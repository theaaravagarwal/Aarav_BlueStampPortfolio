# SmartSole

The SmartSole is a smart shoe sole designed to monitor physical activity by tracking steps, jumps, and running patterns using embedded sensors. It provides alerts through sound or vibrations.

<!-- Replace this text with a brief description (2-3 sentences) of your project. This description should draw the reader in and make them interested in what you've built. You can include what the biggest challenges, takeaways, and triumphs from completing the project were. As you complete your portfolio, remember your audience is less familiar than you are with all that your project entails! -->

<!-- You should comment out all portions of your portfolio that you have not completed yet, as well as any instructions: -->

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Aarav A | Stratford Preparatory | Computer Science | Incoming Sophomore

<!-- **Replace the BlueStamp logo below with an image of yourself and your completed project. Follow the guide [here](https://tomcam.github.io/least-github-pages/adding-images-github-pages-site.html) if you need help.** -->

<!-- ![Headstone Image](logo.svg) -->

# Final Milestone

### Description

### Challenges

### Next Steps

<!-- **Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

For your final milestone, explain the outcome of your project. Key details to include are:

- What you've accomplished since your previous milestone
- What your biggest challenges and triumphs were at BSE
- A summary of key topics you learned about
- What you hope to learn in the future after everything you've learned at BSE -->

# Second Milestone

### Description

### Challenges

### Next Steps

<!-- **Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

For your second milestone, explain what you've worked on since your previous milestone. You can highlight:

- Technical details of what you've accomplished and how they contribute to the final goal
- What has been surprising about the project so far
- Previous challenges you faced that you overcame
- What needs to be completed before your final milestone -->

# First Milestone



### Description

In my first milestone, I focused on the algorithms that would power my project in the future. I built a few algorithms:

    - Movement Detection
    - Step Detection
    - Distance Estimation
    - FSR Variance

1. Movement Detection

    This algorithm is primarily used for power optimization. For example, if we know the user is not moving we do not need to check if they are taking a step as they must be moving to take a step. This algorithm starts by calculating the the change in pitch and roll since the last iteration. Then it checks if the change in pitch and roll exceeds some threshold value in degrees. In much simpler terms, if the accelerometer moves a certain amount of degrees it will be marked as moving. Some challenges I encountered while developing this algorithm were the AHRS (Attitude and Heading Reference System) not correctly calculating the accelerometer's position as well as not being accurate.

    ```cpp
    static float lastRoll = roll, lastPitch = pitch;            //values to find the respective delta values

    const float threshold = 5.0f;                               //degrees, the amount of movement required to register movement

    float deltaRoll = fabs(roll-lastRoll);                      //we take the delta roll

    float deltaPitch = fabs(pitch-lastPitch);                   //then we take the delta pitch

    if (deltaRoll>threshold||deltaPitch>threshold) {
                                                                //the above line checks if either delta pitch or 
                                                                //delta roll exceeds the threshold

        if (!isMoving) {                                        //if we are not already moving

            isMoving = 1;                                       //if we have exceeded the threshold then we must be moving
                                                                //so our flag must be true here

                                                                //an action can be performed here
        }
    } else {                                                    //otherwise

        if (isMoving) {                                         //if we are moving

            isMoving = 0;                                       //this is set to false so that next iteration we can
                                                                //still detect movement as not changing it would be a
                                                                //1 way switch rather than a 2 way switch

                                                                //an action can be performed here as well
        }
    }
    lastRoll = roll;                                            //shift last roll for the next iteration
    lastPitch = pitch;                                          //shift last pitch for next iteration
    ```

    **Time Complexity:** $$O\left(1\right)$$

    **Space Complexity:** $$O\left(1\right)$$

2. Step Detection

    This algorithm is used to estimate distance currently and will be used in the future to estimate health. It serves as a step detection algorithm using accelerometer data. The algorithm computes the magnitude of the acceleration vector and estimates the gravitational component. This gravity estimate is subtracted from the raw magnitude to obtain a filtered signal representing the true acceleration. The algorithm then calculates a dynamic threshold based on the average magnitude of recent samples. The algorithm looks for valleys and peaks in the filtered signal that meet specific criteria for step detection: the amplitude must exceed the threshold, the time interval between steps must be less than around 250 ms, and a valid valley must precede the peak. When all these conditions are satisfied, a step is registered. I encountered a lot of challenges when developing this algorithm such as the math behind the low pass filter, and implementing the gravity filtration with the AHRS gravity filtration system.

    ```cpp
    void update(const sensors_event_t& accel) {
        float magnitude = sqrt(
            accel.acceleration.x * accel.acceleration.x +
            accel.acceleration.y * accel.acceleration.y +
            accel.acceleration.z * accel.acceleration.z        //we calculate the magnitude of acceleration using sqrt(ax^2 + ay^2 + az^2)
        );

        gravity = alpha * gravity + (1 - alpha) * magnitude;   //then we apply low pass filter to estimate gravity

        float filteredMagnitude = magnitude - gravity;         //we remove gravity from raw acceleration to get filtered magnitude

        sum += fabs(filteredMagnitude);                        //then accumulate the absolute filtered magnitude (for average)
        count++;                                               //increment the sample count (for average)

        if (cnt>=50) {                                         //every 50 samples, update the dynamic threshold (50 is arbitrary)
            float average = sum / count;                       //we get the average magnitude
            threshold = baseThreshold + average * 0.2f;        //then we set the threshold based on baseline and average
            sum = 0.0f; count = 0;                             //finally reset sum and count for next window
        }

        unsigned long now = millis();                          //we get current time in milliseconds

        static float lastValley = 0.0f;                        //last valley value, initialized to 0, could also be -inf
        static float lastPeak = 0.0f;                          //last peak value, initialized to 0, could also be -inf
        
        static bool detectValley = false;                      //a flag for detecting a valley

        //detect valley: previous magnitude > last magnitude < current filtered magnitude, and last magnitude is less than 
        if (previousMagnitude > lastMagnitude && lastMagnitude < filteredMagnitude && lastMagnitude < -threshold * 0.5f) {
            lastValley = lastMagnitude; detectValley = true;
        }

        //detect peak: previous magnitude < last magnitude > current filtered magnitude, and last magnitude exceeds threshold
        bool detectPeak = (previousMagnitude < lastMagnitude) && (lastMagnitude > filteredMagnitude) && (lastMagnitude > threshold);

        bool amplitudeOk = (lastMagnitude - lastValley) > (threshold * 0.5f); //check if amplitude between last peak and last valley is above threshold

        //iff a valid peak is detected, amplitude is sufficient, enough time has passed since the last step, and a valley was detected
        if (detectPeak && amplitudeOk && (now - lastStepTime) > minStepInterval && detectValley) {
            lastStepTime = now;                                //we update last step time

            stepCount++;                                       //then increment step count

            detectValley = false;                              //then reset valley detection flag

            lastPeak = lastMagnitude;                          //we store last peak value
        }

        previousMagnitude = lastMagnitude;                     //finally update previous magnitude for next iteration
        lastMagnitude = filteredMagnitude;                     //and update last magnitude for next iteration
    }
    ```

    **Time Complexity:** $$O\left(1\right)$$

    **Space Complexity:** $$O\left(1\right)$$

3. Distance Estimation

    This algorithm is

    ```cpp
    float strideLength = 0.7f;                                  //initial stride length   (meters)
    float distance = 0.0f;                                      //initial total distance  (meters)

    int stepCount = pedometer.getStepCount();                   //we get the current step count from the pedometer
    int lastStepCount = 0;                                      //initialize our last step count so we can compare

    static float maxLinearMagnitude = 0.0f;                     //we also need to the maximum linear acceleration magnitude since the last step

                                                                //we update the maximum linear magnitude if the current value is higher
    if (linearMagnitude > maxLinearMagnitude)
        maxLinearMagnitude = linearMagnitude;                   //set the new higher value as the new max

    if (stepCount > lastStepCount) {                            //if a new step has been detected (step count increased)
                                                                //we will be estimating step length based on the peak acceleration (maxLinearMagnitude)
                                                                //formula: base length + scale * (peak acceleration - 1g)

        float newStrideLength = 0.45f + 0.25f * (maxLinearMagnitude / 9.80665f - 1.0f);

        if (newStrideLength < 0.3f) newStrideLength = 0.3f;     //lower bound clamp
        if (newStrideLength > 1.2f) newStrideLength = 1.2f;     //upper bound clamp

        stlen = dst;

                                                                //calculate how many steps were taken since the last update
        int StepsTaken = stepCount - lastStepCount;

        distance += stepsTaken * strideLength;                  //add the distance for these steps to the total distance

        lastStepCount = stepCount;                              //update the last step count

        maxLinearMagnitude = 0.0f;                              //finally reset the maximum linear magnitude for the next iteration
    }
    ```

    **Time Complexity:** $$O\left(1\right)$$
    **Space Complexity:** $$O\left(1\right)$$

4. FSR Variance

    This algorithm is used to measure 

    why             ∆
    how             ∆
    summary         ∆
    challenges      ∆

    ```cpp
    
    ```

    **Time Complexity:** $$O\left(n^{2}\right)$$

    **Space Complexity:** $$O\left(n\right)$$

### Challenges

### Next Steps

<!-- **Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

For your first milestone, describe what your project is and how you plan to build it. You can include:

- An explanation about the different components of your project and how they will all integrate together
- Technical progress you've made so far
- Challenges you're facing and solving in your future milestones
- What your plan is to complete your project -->

# Starter Milestone

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/2HmSv4AucCM?si=lUCH4t8UGWBSdCUS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Description

My starter project is a retro arcade console that allows the user to play classic video games like Tetris, Snake, and Space Invaders. The screen is constructed from two 8x8 dot matrices on the top left and has a screen capable of displaying three digits in the top right. The system can be powered by the battery pack on the back of the device or by using the Micro USB port near to the number screen. The device creates sound by using a buzzer below the red power switch. There are six yellow buttons below those components which control the elements on the screen in various games.

<img src="assets/image.png" alt="Device Image" width="350" style="flex: 1; border-radius: 8px; margin-left: 16px;"/>

### Challenges

Some challenges I encountered while working on this project were properly soldering the parts to the board as it was time consuming and was the hardest part of this project. I also discovered near the end of the project that I had attached the battery pack backwards and had to spend time fixing my mistake.

### Next Steps

I will begin working on my intensive project after this Starter Milestone.

# Schematics

<!-- Here's where you'll put images of your schematics. [Tinkercad](https://www.tinkercad.com/blog/official-guide-to-tinkercad-circuits) and [Fritzing](https://fritzing.org/learning/) are both great resoruces to create professional schematic diagrams, though BSE recommends Tinkercad becuase it can be done easily and for free in the browser. -->

# Bill of Materials

<!-- Here's where you'll list the parts in your project. To add more rows, just copy and paste the example rows below.
Don't forget to place the link of where to buy each component inside the quotation marks in the corresponding row after href =. Follow the guide [here]([url](https://www.markdownguide.org/extended-syntax/)) to learn how to customize this to your project needs. -->

| **Part** | **Note** | **Price** | **Link** |
|:--:|:--:|:--:|:--:|
| ESP32 C3 Mini | Main microcontroller for processing sensor data and handling communication | $Price | <a href="https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/"> Link </a> |
| MPU-6050 IMU Module | Measures acceleration and gyroscopic data to detect steps, jumps, and running | $Price | <a href="https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/"> Link </a> |
| FSR Sensor | Detects pressure changes to monitor footfalls and activity intensity | $Price | <a href="https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/"> Link </a> |
| TP4056 USB-C Charging Module | To charge the battery with USB-C | $Price | <a href="https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/"> Link </a> |
| Buzzer Module | Emits sound alerts for user notifications | $Price | <a href="https://www.digikey.com/en/products/detail/tdk-corporation/PS1720P02/935932?gad_source=1&gad_campaignid=20243136172&gbraid=0AAAAADrbLlghND7nveKo8z1cOduDoowfF&gclid=CjwKCAjwi-DBBhA5EiwAXOHsGYRiIKDfOIqLUmEYs8KGo-pb2CEg-UOhGTu9yFSsHdKHqSCr81CThhoCiZ0QAvD_BwE&gclsrc=aw.ds"> Link </a> |
| Vibration Motor Module | Gives haptic feedback to alert the user while running | $Price | <a href="https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/"> Link </a> |
| Flexible PCB | Integrates all electronic components into a flexible form factor suitable for insoles that are constantly changing shape | $Price | <a href="https://www.amazon.com/protoboard-Flexible-breadboard-Circuit-Prototype/dp/B0DFVFDX2V/ref=sr_1_3?crid=1NN6H1CZQWEUW&dib=eyJ2IjoiMSJ9.fgCSooY7xlzVsaXztNDIuxlNaJUvbCUCuF4TOwFaVtqZ53VmWMPX0cUistKDt5DjzE5UrWVCI85zAbxqtQTXOPTKupGqLMceeb5ok34VYuULCEBCG9p-31KL-eH7utkBGQZRzicobyLrjHf2Rc7zgXc2btx_52IjSXu8MuWHSC44peVL4UxVwIkVOknTf95VItoxV3Mu734_2YHuGfRWl76kL9tASuy0RCwSU7VbyqQ.VACdPynqQkaPo9Pi2N4Ms1JdLqukNUEQ1sw_sLpEAT0&dib_tag=se&keywords=Flexible+Protoboard&qid=1748543175&sprefix=flexible+protoboard%2Caps%2C90&sr=8-3"> Link </a> |

<!-- # Other Resources/Examples (not needed?)

One of the best parts about Github is that you can view how other people set up their own work. Here are some past BSE portfolios that are awesome examples. You can view how they set up their portfolio, and you can view their index.md files to understand how they implemented different portfolio components.

- [Example 1](https://trashytuber.github.io/YimingJiaBlueStamp/)
- [Example 2](https://sviatil0.github.io/Sviatoslav_BSE/)
- [Example 3](https://arneshkumar.github.io/arneshbluestamp/)

To watch the BSE tutorial on how to create a portfolio, click here. -->

<!-- quicklink: (https://theaaravagarwal.github.io/Aarav_BlueStampPortfolio) -->

<!-- <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script> -->

<!-- <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> -->

<!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML" type="text/javascript"></script> -->

<!-- <script type="text/javascript" charset="utf-8" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://vincenttam.github.io/javascripts/MathJaxLocal.js"></script> -->

<!-- <html><head><script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script></head></html> -->x