# SmartSole

The SmartSole is a smart shoe sole designed to monitor physical activity by tracking steps, jumps, and running patterns using embedded sensors. It provides alerts through sound or vibrations.

<!-- Replace this text with a brief description (2-3 sentences) of your project. This description should draw the reader in and make them interested in what you've built. You can include what the biggest challenges, takeaways, and triumphs from completing the project were. As you complete your portfolio, remember your audience is less familiar than you are with all that your project entails! -->

<!-- You should comment out all portions of your portfolio that you have not completed yet, as well as any instructions: -->

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| **Aarav A** | Stratford Preparatory | Computer Science | Incoming Sophomore |

<!-- **Replace the BlueStamp logo below with an image of yourself and your completed project. Follow the guide [here](https://tomcam.github.io/least-github-pages/adding-images-github-pages-site.html) if you need help.** -->

<!-- ![Headstone Image](logo.svg) -->

# Third Milestone



### Description

My final milestone focused on the final assembly of my product. In this milestone I created various 3D prints, like casings for my battery pack and ESP32. I also made various clip designs to attach the product components to. In the end I attached the battery to a ankle strap made of velcro and only used the clip for the ESP32. I also attached the FSR to the insole of the shoe with tape. I utilized the flex PCB to handle the connections from the ESP32 to the FSR.

### 3D Prints

In this milestone, I designed and printed several custom 3D parts to house and protect the electronics. These included casings for the battery pack and ESP32, as well as various clip designs to securely attach components to the shoe and ankle strap. The final design used a clip for the ESP32 and a custom battery case attached to a velcro ankle strap for comfort and stability.

```stl
solid OpenSCAD_Model
  facet normal 0.454018 -0.890992 0
    outer loop
      vertex 4.02527 -3.4258 0
      vertex 4.375 -3.24759 25
      vertex 4.02527 -3.4258 25
    endloop
  endfacet
  facet normal 0.454018 -0.890992 0
    outer loop
      vertex 4.375 -3.24759 25
      vertex 4.02527 -3.4258 0
      vertex 4.375 -3.24759 0
    endloop
  endfacet
  facet normal 0.751822 0.659366 0
    outer loop
      vertex 4.46683 54.305 25
      vertex 4.20802 54.6001 0
      vertex 4.20802 54.6001 25
    endloop
  endfacet
  facet normal 0.751822 0.659366 0
    outer loop
      vertex 4.20802 54.6001 0
      vertex 4.46683 54.305 25
      vertex 4.46683 54.305 0
    endloop
  endfacet
  facet normal -0.987689 -0.156428 0
    outer loop
      vertex -6.16806 -0.779663 0
      vertex -6.22946 -0.391983 25
      vertex -6.22946 -0.391983 0
    endloop
  endfacet
  facet normal -0.987689 -0.156428 0
    outer loop
      vertex -6.22946 -0.391983 25
      vertex -6.16806 -0.779663 0
      vertex -6.16806 -0.779663 25
    endloop
  endfacet
  facet normal -0.544642 -0.838669 0
    outer loop
      vertex -4.70419 -3.03381 0
      vertex -4.375 -3.24759 25
      vertex -4.70419 -3.03381 25
    endloop
  endfacet
  facet normal -0.544642 -0.838669 -0
    outer loop
      vertex -4.375 -3.24759 25
      vertex -4.70419 -3.03381 0
      vertex -4.375 -3.24759 0
    endloop
  endfacet
  facet normal 0.269487 0.963004 -0
    outer loop
      vertex 1.70967 56.0115 0
      vertex 1.65714 56.0262 25
      vertex 1.70967 56.0115 25
    endloop
  endfacet
  facet normal 0.269487 0.963004 0
    outer loop
      vertex 1.65714 56.0262 25
      vertex 1.70967 56.0115 0
      vertex 1.65714 56.0262 0
    endloop
  endfacet
  facet normal 1 -0 0
    outer loop
      vertex 6.25 0 25
      vertex 6.25 50 0
      vertex 6.25 50 25
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 6.25 50 0
      vertex 6.25 0 25
      vertex 6.25 0 0
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex -6.25 0 0
      vertex -6.25 50 25
      vertex -6.25 50 0
    endloop
  endfacet
  facet normal -1 -0 0
    outer loop
      vertex -6.25 50 25
      vertex -6.25 0 0
      vertex -6.25 0 25
    endloop
  endfacet
  facet normal -0.258802 -0.96593 0
    outer loop
      vertex -3.65881 -3.56647 0
      vertex -3.5 -3.60902 25
      vertex -3.65881 -3.56647 25
    endloop
  endfacet
  facet normal -0.258802 -0.96593 -0
    outer loop
      vertex -3.5 -3.60902 25
      vertex -3.65881 -3.56647 0
      vertex -3.5 -3.60902 0
    endloop
  endfacet
  facet normal -0.777162 -0.629301 0
    outer loop
      vertex -5.28679 -2.50925 0
      vertex -5.53381 -2.20419 25
      vertex -5.53381 -2.20419 0
    endloop
  endfacet
  facet normal -0.777162 -0.629301 0
    outer loop
      vertex -5.53381 -2.20419 25
      vertex -5.28679 -2.50925 0
      vertex -5.28679 -2.50925 25
    endloop
  endfacet
  facet normal -0.890992 -0.454018 0
    outer loop
      vertex -5.74759 -1.875 0
      vertex -5.9258 -1.52527 25
      vertex -5.9258 -1.52527 0
    endloop
  endfacet
  facet normal -0.890992 -0.454018 0
    outer loop
      vertex -5.9258 -1.52527 25
      vertex -5.74759 -1.875 0
      vertex -5.74759 -1.875 25
    endloop
  endfacet
  facet normal 0.383089 0.923711 -0
    outer loop
      vertex 2.42934 55.7584 0
      vertex 2.35411 55.7896 25
      vertex 2.42934 55.7584 25
    endloop
  endfacet
  facet normal 0.383089 0.923711 0
    outer loop
      vertex 2.35411 55.7896 25
      vertex 2.42934 55.7584 0
      vertex 2.35411 55.7896 0
    endloop
  endfacet
  facet normal 0.99863 -0.0523284 0
    outer loop
      vertex 6.22946 -0.391983 25
      vertex 6.25 0 0
      vertex 6.25 0 25
    endloop
  endfacet
  facet normal 0.99863 -0.0523284 0
    outer loop
      vertex 6.25 0 0
      vertex 6.22946 -0.391983 25
      vertex 6.22946 -0.391983 0
    endloop
  endfacet
  facet normal 0.56473 0.825276 -0
    outer loop
      vertex 3.55119 55.143 0
      vertex 3.50618 55.1738 25
      vertex 3.55119 55.143 25
    endloop
  endfacet
  facet normal 0.56473 0.825276 0
    outer loop
      vertex 3.50618 55.1738 25
      vertex 3.55119 55.143 0
      vertex 3.50618 55.1738 0
    endloop
  endfacet
  facet normal 0.129912 0.991525 -0
    outer loop
      vertex 0.856201 56.191 0
      vertex 0.775299 56.2016 25
      vertex 0.856201 56.191 25
    endloop
  endfacet
  facet normal 0.129912 0.991525 0
    outer loop
      vertex 0.775299 56.2016 25
      vertex 0.856201 56.191 0
      vertex 0.775299 56.2016 0
    endloop
  endfacet
  facet normal 0.582797 0.812617 -0
    outer loop
      vertex 3.66228 55.0645 0
      vertex 3.61794 55.0963 25
      vertex 3.66228 55.0645 25
    endloop
  endfacet
  facet normal 0.582797 0.812617 0
    outer loop
      vertex 3.61794 55.0963 25
      vertex 3.66228 55.0645 0
      vertex 3.61794 55.0963 0
    endloop
  endfacet
  facet normal 0.0219907 0.999758 -0
    outer loop
      vertex 0.177292 56.2474 0
      vertex 0.095459 56.2492 25
      vertex 0.177292 56.2474 25
    endloop
  endfacet
  facet normal 0.0219907 0.999758 0
    outer loop
      vertex 0.095459 56.2492 25
      vertex 0.177292 56.2474 0
      vertex 0.095459 56.2492 0
    endloop
  endfacet
  facet normal -0.99741 0.0719188 0
    outer loop
      vertex -6.25 50 0
      vertex -6.2112 50.5381 25
      vertex -6.2112 50.5381 0
    endloop
  endfacet
  facet normal -0.99741 0.0719188 0
    outer loop
      vertex -6.2112 50.5381 25
      vertex -6.25 50 0
      vertex -6.25 50 25
    endloop
  endfacet
  facet normal -0.1082 0.994129 0
    outer loop
      vertex -0.639374 56.2171 0
      vertex -0.721146 56.2082 25
      vertex -0.639374 56.2171 25
    endloop
  endfacet
  facet normal -0.1082 0.994129 0
    outer loop
      vertex -0.721146 56.2082 25
      vertex -0.639374 56.2171 0
      vertex -0.721146 56.2082 0
    endloop
  endfacet
  facet normal -0.629301 -0.777162 0
    outer loop
      vertex -5.00925 -2.78679 0
      vertex -4.70419 -3.03381 25
      vertex -5.00925 -2.78679 25
    endloop
  endfacet
  facet normal -0.629301 -0.777162 -0
    outer loop
      vertex -4.70419 -3.03381 25
      vertex -5.00925 -2.78679 0
      vertex -4.70419 -3.03381 0
    endloop
  endfacet
  facet normal -0.432636 0.901569 0
    outer loop
      vertex -2.67839 55.6469 0
      vertex -2.72757 55.6233 25
      vertex -2.67839 55.6469 25
    endloop
  endfacet
  facet normal -0.432636 0.901569 0
    outer loop
      vertex -2.72757 55.6233 25
      vertex -2.67839 55.6469 0
      vertex -2.72757 55.6233 0
    endloop
  endfacet
  facet normal 0.816602 0.577201 0
    outer loop
      vertex 4.69337 53.9845 25
      vertex 4.46683 54.305 0
      vertex 4.46683 54.305 25
    endloop
  endfacet
  facet normal 0.816602 0.577201 0
    outer loop
      vertex 4.46683 54.305 0
      vertex 4.69337 53.9845 25
      vertex 4.69337 53.9845 0
    endloop
  endfacet
  facet normal -0.599736 0.800198 0
    outer loop
      vertex -3.7281 55.0162 0
      vertex -3.77173 54.9835 25
      vertex -3.7281 55.0162 25
    endloop
  endfacet
  facet normal -0.599736 0.800198 0
    outer loop
      vertex -3.77173 54.9835 25
      vertex -3.7281 55.0162 0
      vertex -3.77173 54.9835 0
    endloop
  endfacet
  facet normal -0.99863 -0.0523284 0
    outer loop
      vertex -6.22946 -0.391983 0
      vertex -6.25 0 25
      vertex -6.25 0 0
    endloop
  endfacet
  facet normal -0.99863 -0.0523284 0
    outer loop
      vertex -6.25 0 25
      vertex -6.22946 -0.391983 0
      vertex -6.22946 -0.391983 25
    endloop
  endfacet
  facet normal -0.859899 0.510464 0
    outer loop
      vertex -4.88516 53.642 0
      vertex -4.5887 54.1414 25
      vertex -4.5887 54.1414 0
    endloop
  endfacet
  facet normal -0.859899 0.510464 0
    outer loop
      vertex -4.5887 54.1414 25
      vertex -4.88516 53.642 0
      vertex -4.88516 53.642 25
    endloop
  endfacet
  facet normal 0.707107 -0.707107 0
    outer loop
      vertex 5.00925 -2.78679 25
      vertex 5.28679 -2.50925 0
      vertex 5.28679 -2.50925 25
    endloop
  endfacet
  facet normal 0.707107 -0.707107 0
    outer loop
      vertex 5.28679 -2.50925 0
      vertex 5.00925 -2.78679 25
      vertex 5.00925 -2.78679 0
    endloop
  endfacet
  facet normal -0.838669 -0.544642 0
    outer loop
      vertex -5.53381 -2.20419 0
      vertex -5.74759 -1.875 25
      vertex -5.74759 -1.875 0
    endloop
  endfacet
  facet normal -0.838669 -0.544642 0
    outer loop
      vertex -5.74759 -1.875 25
      vertex -5.53381 -2.20419 0
      vertex -5.53381 -2.20419 25
    endloop
  endfacet
  facet normal 0.926366 0.376626 0
    outer loop
      vertex 6.06647 51.1588 25
      vertex 5.86327 51.6586 0
      vertex 5.86327 51.6586 25
    endloop
  endfacet
  facet normal 0.926366 0.376626 0
    outer loop
      vertex 5.86327 51.6586 0
      vertex 6.06647 51.1588 25
      vertex 6.06647 51.1588 0
    endloop
  endfacet
  facet normal -0.358366 -0.933581 0
    outer loop
      vertex -4.02527 -3.4258 0
      vertex -3.65881 -3.56647 25
      vertex -4.02527 -3.4258 25
    endloop
  endfacet
  facet normal -0.358366 -0.933581 -0
    outer loop
      vertex -3.65881 -3.56647 25
      vertex -4.02527 -3.4258 0
      vertex -3.65881 -3.56647 0
    endloop
  endfacet
  facet normal -0.896872 0.442291 0
    outer loop
      vertex -5.86327 51.6586 0
      vertex -4.88516 53.642 25
      vertex -4.88516 53.642 0
    endloop
  endfacet
  facet normal -0.896872 0.442291 0
    outer loop
      vertex -4.88516 53.642 25
      vertex -5.86327 51.6586 0
      vertex -5.86327 51.6586 25
    endloop
  endfacet
  facet normal -0.980781 0.195112 0
    outer loop
      vertex -6.2112 50.5381 0
      vertex -6.13461 50.9231 25
      vertex -6.13461 50.9231 0
    endloop
  endfacet
  facet normal -0.980781 0.195112 0
    outer loop
      vertex -6.13461 50.9231 25
      vertex -6.2112 50.5381 0
      vertex -6.2112 50.5381 25
    endloop
  endfacet
  facet normal 0.896872 0.442291 0
    outer loop
      vertex 5.86327 51.6586 25
      vertex 4.88516 53.642 0
      vertex 4.88516 53.642 25
    endloop
  endfacet
  facet normal 0.896872 0.442291 0
    outer loop
      vertex 4.88516 53.642 0
      vertex 5.86327 51.6586 25
      vertex 5.86327 51.6586 0
    endloop
  endfacet
  facet normal 0.965919 0.258844 0
    outer loop
      vertex 6.16806 50.7797 25
      vertex 6.06647 51.1588 0
      vertex 6.06647 51.1588 25
    endloop
  endfacet
  facet normal 0.965919 0.258844 0
    outer loop
      vertex 6.06647 51.1588 0
      vertex 6.16806 50.7797 25
      vertex 6.16806 50.7797 0
    endloop
  endfacet
  facet normal -0.0862998 0.996269 0
    outer loop
      vertex -0.504288 56.2295 0
      vertex -0.585098 56.2225 25
      vertex -0.504288 56.2295 25
    endloop
  endfacet
  facet normal -0.0862998 0.996269 0
    outer loop
      vertex -0.585098 56.2225 25
      vertex -0.504288 56.2295 0
      vertex -0.585098 56.2225 0
    endloop
  endfacet
  facet normal -0.454018 -0.890992 0
    outer loop
      vertex -4.375 -3.24759 0
      vertex -4.02527 -3.4258 25
      vertex -4.375 -3.24759 25
    endloop
  endfacet
  facet normal -0.454018 -0.890992 -0
    outer loop
      vertex -4.02527 -3.4258 25
      vertex -4.375 -3.24759 0
      vertex -4.02527 -3.4258 0
    endloop
  endfacet
  facet normal 0.320783 0.947153 -0
    outer loop
      vertex 2.04782 55.9049 0
      vertex 1.96928 55.9315 25
      vertex 2.04782 55.9049 25
    endloop
  endfacet
  facet normal 0.320783 0.947153 0
    outer loop
      vertex 1.96928 55.9315 25
      vertex 2.04782 55.9049 0
      vertex 1.96928 55.9315 0
    endloop
  endfacet
  facet normal 0.660108 0.75117 -0
    outer loop
      vertex 4.20802 54.6001 0
      vertex 3.77173 54.9835 25
      vertex 4.20802 54.6001 25
    endloop
  endfacet
  facet normal 0.660108 0.75117 0
    outer loop
      vertex 3.77173 54.9835 25
      vertex 4.20802 54.6001 0
      vertex 3.77173 54.9835 0
    endloop
  endfacet
  facet normal -0.259162 0.965834 0
    outer loop
      vertex -1.57776 56.0475 0
      vertex -1.65714 56.0262 25
      vertex -1.57776 56.0475 25
    endloop
  endfacet
  facet normal -0.259162 0.965834 0
    outer loop
      vertex -1.65714 56.0262 25
      vertex -1.57776 56.0475 0
      vertex -1.65714 56.0262 0
    endloop
  endfacet
  facet normal -0.372276 0.928122 0
    outer loop
      vertex -2.3035 55.8099 0
      vertex -2.35411 55.7896 25
      vertex -2.3035 55.8099 25
    endloop
  endfacet
  facet normal -0.372276 0.928122 0
    outer loop
      vertex -2.35411 55.7896 25
      vertex -2.3035 55.8099 0
      vertex -2.35411 55.7896 0
    endloop
  endfacet
  facet normal -0.129912 0.991525 0
    outer loop
      vertex -0.775299 56.2016 0
      vertex -0.856201 56.191 25
      vertex -0.775299 56.2016 25
    endloop
  endfacet
  facet normal -0.129912 0.991525 0
    outer loop
      vertex -0.856201 56.191 25
      vertex -0.775299 56.2016 0
      vertex -0.856201 56.191 0
    endloop
  endfacet
  facet normal 0.99863 0.0523262 0
    outer loop
      vertex 6.25 50 25
      vertex 6.22946 50.392 0
      vertex 6.22946 50.392 25
    endloop
  endfacet
  facet normal 0.99863 0.0523262 0
    outer loop
      vertex 6.22946 50.392 0
      vertex 6.25 50 25
      vertex 6.25 50 0
    endloop
  endfacet
  facet normal 0.372276 0.928122 -0
    outer loop
      vertex 2.35411 55.7896 0
      vertex 2.3035 55.8099 25
      vertex 2.35411 55.7896 25
    endloop
  endfacet
  facet normal 0.372276 0.928122 0
    outer loop
      vertex 2.3035 55.8099 25
      vertex 2.35411 55.7896 0
      vertex 2.3035 55.8099 0
    endloop
  endfacet
  facet normal 0.987691 0.15642 0
    outer loop
      vertex 6.22946 50.392 25
      vertex 6.16806 50.7797 0
      vertex 6.16806 50.7797 25
    endloop
  endfacet
  facet normal 0.987691 0.15642 0
    outer loop
      vertex 6.16806 50.7797 0
      vertex 6.22946 50.392 25
      vertex 6.22946 50.392 0
    endloop
  endfacet
  facet normal -0.933581 -0.358366 0
    outer loop
      vertex -5.9258 -1.52527 0
      vertex -6.06647 -1.15881 25
      vertex -6.06647 -1.15881 0
    endloop
  endfacet
  facet normal -0.933581 -0.358366 0
    outer loop
      vertex -6.06647 -1.15881 25
      vertex -5.9258 -1.52527 0
      vertex -5.9258 -1.52527 25
    endloop
  endfacet
  facet normal -0.918809 0.394703 0
    outer loop
      vertex -6.01822 51.2979 0
      vertex -5.86327 51.6586 25
      vertex -5.86327 51.6586 0
    endloop
  endfacet
  facet normal -0.918809 0.394703 0
    outer loop
      vertex -5.86327 51.6586 25
      vertex -6.01822 51.2979 0
      vertex -6.01822 51.2979 25
    endloop
  endfacet
  facet normal 0 1 -0
    outer loop
      vertex 0.0409241 56.2498 0
      vertex -0.0409241 56.2498 25
      vertex 0.0409241 56.2498 25
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -0.0409241 56.2498 25
      vertex 0.0409241 56.2498 0
      vertex -0.0409241 56.2498 0
    endloop
  endfacet
  facet normal -0.786638 0.617414 0
    outer loop
      vertex -4.5887 54.1414 0
      vertex -4.34633 54.4502 25
      vertex -4.34633 54.4502 0
    endloop
  endfacet
  facet normal -0.786638 0.617414 0
    outer loop
      vertex -4.34633 54.4502 25
      vertex -4.5887 54.1414 0
      vertex -4.5887 54.1414 25
    endloop
  endfacet
  facet normal 0.872517 0.488584 0
    outer loop
      vertex 4.88516 53.642 25
      vertex 4.69337 53.9845 0
      vertex 4.69337 53.9845 25
    endloop
  endfacet
  facet normal 0.872517 0.488584 0
    outer loop
      vertex 4.69337 53.9845 0
      vertex 4.88516 53.642 25
      vertex 4.88516 53.642 0
    endloop
  endfacet
  facet normal -0.452778 0.891624 0
    outer loop
      vertex -2.80121 55.587 0
      vertex -2.84985 55.5623 25
      vertex -2.80121 55.587 25
    endloop
  endfacet
  facet normal -0.452778 0.891624 0
    outer loop
      vertex -2.84985 55.5623 25
      vertex -2.80121 55.587 0
      vertex -2.84985 55.5623 0
    endloop
  endfacet
  facet normal -0.707107 -0.707107 0
    outer loop
      vertex -5.00925 -2.78679 0
      vertex -5.28679 -2.50925 25
      vertex -5.28679 -2.50925 0
    endloop
  endfacet
  facet normal -0.707107 -0.707107 0
    outer loop
      vertex -5.28679 -2.50925 25
      vertex -5.00925 -2.78679 0
      vertex -5.00925 -2.78679 25
    endloop
  endfacet
  facet normal -0.491157 0.871071 0
    outer loop
      vertex -3.0416 55.4599 0
      vertex -3.08913 55.4331 25
      vertex -3.0416 55.4599 25
    endloop
  endfacet
  facet normal -0.491157 0.871071 0
    outer loop
      vertex -3.08913 55.4331 25
      vertex -3.0416 55.4599 0
      vertex -3.08913 55.4331 0
    endloop
  endfacet
  facet normal 0.363181 0.931718 -0
    outer loop
      vertex 2.3035 55.8099 0
      vertex 2.22705 55.8397 25
      vertex 2.3035 55.8099 25
    endloop
  endfacet
  facet normal 0.363181 0.931718 0
    outer loop
      vertex 2.22705 55.8397 25
      vertex 2.3035 55.8099 0
      vertex 2.22705 55.8397 0
    endloop
  endfacet
  facet normal -0.442139 0.896946 0
    outer loop
      vertex -2.72757 55.6233 0
      vertex -2.80121 55.587 25
      vertex -2.72757 55.6233 25
    endloop
  endfacet
  facet normal -0.442139 0.896946 0
    outer loop
      vertex -2.80121 55.587 25
      vertex -2.72757 55.6233 0
      vertex -2.80121 55.587 0
    endloop
  endfacet
  facet normal 0.247581 0.968867 -0
    outer loop
      vertex 1.57776 56.0475 0
      vertex 1.52493 56.061 25
      vertex 1.57776 56.0475 25
    endloop
  endfacet
  facet normal 0.247581 0.968867 0
    outer loop
      vertex 1.52493 56.061 25
      vertex 1.57776 56.0475 0
      vertex 1.52493 56.061 0
    endloop
  endfacet
  facet normal -0.0990027 0.995087 0
    outer loop
      vertex -0.585098 56.2225 0
      vertex -0.639374 56.2171 25
      vertex -0.585098 56.2225 25
    endloop
  endfacet
  facet normal -0.0990027 0.995087 0
    outer loop
      vertex -0.639374 56.2171 25
      vertex -0.585098 56.2225 0
      vertex -0.639374 56.2171 0
    endloop
  endfacet
  facet normal 0.573256 0.819376 -0
    outer loop
      vertex 3.61794 55.0963 0
      vertex 3.55119 55.143 25
      vertex 3.61794 55.0963 25
    endloop
  endfacet
  facet normal 0.573256 0.819376 0
    outer loop
      vertex 3.55119 55.143 25
      vertex 3.61794 55.0963 0
      vertex 3.55119 55.143 0
    endloop
  endfacet
  facet normal -0.0658577 0.997829 0
    outer loop
      vertex -0.368088 56.2391 0
      vertex -0.449905 56.2337 25
      vertex -0.368088 56.2391 25
    endloop
  endfacet
  facet normal -0.0658577 0.997829 0
    outer loop
      vertex -0.449905 56.2337 25
      vertex -0.368088 56.2391 0
      vertex -0.449905 56.2337 0
    endloop
  endfacet
  facet normal -0.955012 0.296568 0
    outer loop
      vertex -6.13461 50.9231 0
      vertex -6.01822 51.2979 25
      vertex -6.01822 51.2979 0
    endloop
  endfacet
  facet normal -0.955012 0.296568 0
    outer loop
      vertex -6.01822 51.2979 25
      vertex -6.13461 50.9231 0
      vertex -6.13461 50.9231 25
    endloop
  endfacet
  facet normal 0.933581 -0.358366 0
    outer loop
      vertex 5.9258 -1.52527 25
      vertex 6.06647 -1.15881 0
      vertex 6.06647 -1.15881 25
    endloop
  endfacet
  facet normal 0.933581 -0.358366 0
    outer loop
      vertex 6.06647 -1.15881 0
      vertex 5.9258 -1.52527 25
      vertex 5.9258 -1.52527 0
    endloop
  endfacet
  facet normal -0.0439495 0.999034 0
    outer loop
      vertex -0.231796 56.2456 0
      vertex -0.313629 56.242 25
      vertex -0.231796 56.2456 25
    endloop
  endfacet
  facet normal -0.0439495 0.999034 0
    outer loop
      vertex -0.313629 56.242 25
      vertex -0.231796 56.2456 0
      vertex -0.313629 56.242 0
    endloop
  endfacet
  facet normal 0.0531757 0.998585 -0
    outer loop
      vertex 0.368088 56.2391 0
      vertex 0.313629 56.242 25
      vertex 0.368088 56.2391 25
    endloop
  endfacet
  facet normal 0.0531757 0.998585 0
    outer loop
      vertex 0.313629 56.242 25
      vertex 0.368088 56.2391 0
      vertex 0.313629 56.242 0
    endloop
  endfacet
  facet normal -0.0330071 0.999455 0
    outer loop
      vertex -0.177292 56.2474 0
      vertex -0.231796 56.2456 25
      vertex -0.177292 56.2474 25
    endloop
  endfacet
  facet normal -0.0330071 0.999455 0
    outer loop
      vertex -0.231796 56.2456 25
      vertex -0.177292 56.2474 0
      vertex -0.231796 56.2456 0
    endloop
  endfacet
  facet normal 0.0439495 0.999034 -0
    outer loop
      vertex 0.313629 56.242 0
      vertex 0.231796 56.2456 25
      vertex 0.313629 56.242 25
    endloop
  endfacet
  facet normal 0.0439495 0.999034 0
    outer loop
      vertex 0.231796 56.2456 25
      vertex 0.313629 56.242 0
      vertex 0.231796 56.2456 0
    endloop
  endfacet
  facet normal 0.311659 0.950194 -0
    outer loop
      vertex 1.96928 55.9315 0
      vertex 1.91745 55.9485 25
      vertex 1.96928 55.9315 25
    endloop
  endfacet
  facet normal 0.311659 0.950194 0
    outer loop
      vertex 1.91745 55.9485 25
      vertex 1.96928 55.9315 0
      vertex 1.91745 55.9485 0
    endloop
  endfacet
  facet normal 0.777162 -0.629301 0
    outer loop
      vertex 5.28679 -2.50925 25
      vertex 5.53381 -2.20419 0
      vertex 5.53381 -2.20419 25
    endloop
  endfacet
  facet normal 0.777162 -0.629301 0
    outer loop
      vertex 5.53381 -2.20419 0
      vertex 5.28679 -2.50925 25
      vertex 5.28679 -2.50925 0
    endloop
  endfacet
  facet normal -0.173891 0.984765 0
    outer loop
      vertex -1.04567 56.1618 0
      vertex -1.12552 56.1477 25
      vertex -1.04567 56.1618 25
    endloop
  endfacet
  facet normal -0.173891 0.984765 0
    outer loop
      vertex -1.12552 56.1477 25
      vertex -1.04567 56.1618 0
      vertex -1.12552 56.1477 0
    endloop
  endfacet
  facet normal 0.216393 0.976306 -0
    outer loop
      vertex 1.39297 56.0927 0
      vertex 1.31221 56.1106 25
      vertex 1.39297 56.0927 25
    endloop
  endfacet
  facet normal 0.216393 0.976306 0
    outer loop
      vertex 1.31221 56.1106 25
      vertex 1.39297 56.0927 0
      vertex 1.31221 56.1106 0
    endloop
  endfacet
  facet normal 0.546464 0.837483 -0
    outer loop
      vertex 3.43892 55.2187 0
      vertex 3.39325 55.2485 25
      vertex 3.43892 55.2187 25
    endloop
  endfacet
  facet normal 0.546464 0.837483 0
    outer loop
      vertex 3.39325 55.2485 25
      vertex 3.43892 55.2187 0
      vertex 3.39325 55.2485 0
    endloop
  endfacet
  facet normal -0.195619 0.98068 0
    outer loop
      vertex -1.17912 56.1377 0
      vertex -1.25883 56.1218 25
      vertex -1.17912 56.1377 25
    endloop
  endfacet
  facet normal -0.195619 0.98068 0
    outer loop
      vertex -1.25883 56.1218 25
      vertex -1.17912 56.1377 0
      vertex -1.25883 56.1218 0
    endloop
  endfacet
  facet normal -0.183403 0.983038 0
    outer loop
      vertex -1.12552 56.1477 0
      vertex -1.17912 56.1377 25
      vertex -1.12552 56.1477 25
    endloop
  endfacet
  facet normal -0.183403 0.983038 0
    outer loop
      vertex -1.17912 56.1377 25
      vertex -1.12552 56.1477 0
      vertex -1.17912 56.1377 0
    endloop
  endfacet
  facet normal -0.320783 0.947153 0
    outer loop
      vertex -1.96928 55.9315 0
      vertex -2.04782 55.9049 25
      vertex -1.96928 55.9315 25
    endloop
  endfacet
  facet normal -0.320783 0.947153 0
    outer loop
      vertex -2.04782 55.9049 25
      vertex -1.96928 55.9315 0
      vertex -2.04782 55.9049 0
    endloop
  endfacet
  facet normal -0.363181 0.931718 0
    outer loop
      vertex -2.22705 55.8397 0
      vertex -2.3035 55.8099 25
      vertex -2.22705 55.8397 25
    endloop
  endfacet
  facet normal -0.363181 0.931718 0
    outer loop
      vertex -2.3035 55.8099 25
      vertex -2.22705 55.8397 0
      vertex -2.3035 55.8099 0
    endloop
  endfacet
  facet normal -0.141201 0.989981 0
    outer loop
      vertex -0.856201 56.191 0
      vertex -0.910187 56.1833 25
      vertex -0.856201 56.191 25
    endloop
  endfacet
  facet normal -0.141201 0.989981 0
    outer loop
      vertex -0.910187 56.1833 25
      vertex -0.856201 56.191 0
      vertex -0.910187 56.1833 0
    endloop
  endfacet
  facet normal 0.237779 0.971319 -0
    outer loop
      vertex 1.52493 56.061 0
      vertex 1.44609 56.0803 25
      vertex 1.52493 56.061 25
    endloop
  endfacet
  facet normal 0.237779 0.971319 0
    outer loop
      vertex 1.44609 56.0803 25
      vertex 1.52493 56.061 0
      vertex 1.44609 56.0803 0
    endloop
  endfacet
  facet normal 0.629301 -0.777162 0
    outer loop
      vertex 4.70419 -3.03381 0
      vertex 5.00925 -2.78679 25
      vertex 4.70419 -3.03381 25
    endloop
  endfacet
  facet normal 0.629301 -0.777162 0
    outer loop
      vertex 5.00925 -2.78679 25
      vertex 4.70419 -3.03381 0
      vertex 5.00925 -2.78679 0
    endloop
  endfacet
  facet normal 0.227322 0.97382 -0
    outer loop
      vertex 1.44609 56.0803 0
      vertex 1.39297 56.0927 25
      vertex 1.44609 56.0803 25
    endloop
  endfacet
  facet normal 0.227322 0.97382 0
    outer loop
      vertex 1.39297 56.0927 25
      vertex 1.44609 56.0803 0
      vertex 1.39297 56.0927 0
    endloop
  endfacet
  facet normal 0.392348 0.919817 -0
    outer loop
      vertex 2.47951 55.737 0
      vertex 2.42934 55.7584 25
      vertex 2.47951 55.737 25
    endloop
  endfacet
  facet normal 0.392348 0.919817 0
    outer loop
      vertex 2.42934 55.7584 25
      vertex 2.47951 55.737 0
      vertex 2.42934 55.7584 0
    endloop
  endfacet
  facet normal -0.717689 0.696364 0
    outer loop
      vertex -4.34633 54.4502 0
      vertex -4.073 54.7319 25
      vertex -4.073 54.7319 0
    endloop
  endfacet
  facet normal -0.717689 0.696364 0
    outer loop
      vertex -4.073 54.7319 25
      vertex -4.34633 54.4502 0
      vertex -4.34633 54.4502 25
    endloop
  endfacet
  facet normal -0.0770007 0.997031 0
    outer loop
      vertex -0.449905 56.2337 0
      vertex -0.504288 56.2295 25
      vertex -0.449905 56.2337 25
    endloop
  endfacet
  facet normal -0.0770007 0.997031 0
    outer loop
      vertex -0.504288 56.2295 25
      vertex -0.449905 56.2337 0
      vertex -0.504288 56.2295 0
    endloop
  endfacet
  facet normal 0.259162 0.965834 -0
    outer loop
      vertex 1.65714 56.0262 0
      vertex 1.57776 56.0475 25
      vertex 1.65714 56.0262 25
    endloop
  endfacet
  facet normal 0.259162 0.965834 0
    outer loop
      vertex 1.57776 56.0475 25
      vertex 1.65714 56.0262 0
      vertex 1.57776 56.0475 0
    endloop
  endfacet
  facet normal 0.331861 0.943328 -0
    outer loop
      vertex 2.09927 55.8868 0
      vertex 2.04782 55.9049 25
      vertex 2.09927 55.8868 25
    endloop
  endfacet
  facet normal 0.331861 0.943328 0
    outer loop
      vertex 2.04782 55.9049 25
      vertex 2.09927 55.8868 0
      vertex 2.04782 55.9049 0
    endloop
  endfacet
  facet normal -0.279533 0.960136 0
    outer loop
      vertex -1.70967 56.0115 0
      vertex -1.78867 55.9885 25
      vertex -1.70967 56.0115 25
    endloop
  endfacet
  facet normal -0.279533 0.960136 0
    outer loop
      vertex -1.78867 55.9885 25
      vertex -1.70967 56.0115 0
      vertex -1.78867 55.9885 0
    endloop
  endfacet
  facet normal 0.358366 -0.933581 0
    outer loop
      vertex 3.65881 -3.56647 0
      vertex 4.02527 -3.4258 25
      vertex 3.65881 -3.56647 25
    endloop
  endfacet
  facet normal 0.358366 -0.933581 0
    outer loop
      vertex 4.02527 -3.4258 25
      vertex 3.65881 -3.56647 0
      vertex 4.02527 -3.4258 0
    endloop
  endfacet
  facet normal -0.582797 0.812617 0
    outer loop
      vertex -3.61794 55.0963 0
      vertex -3.66228 55.0645 25
      vertex -3.61794 55.0963 25
    endloop
  endfacet
  facet normal -0.582797 0.812617 0
    outer loop
      vertex -3.66228 55.0645 25
      vertex -3.61794 55.0963 0
      vertex -3.66228 55.0645 0
    endloop
  endfacet
  facet normal -0.0219907 0.999758 0
    outer loop
      vertex -0.095459 56.2492 0
      vertex -0.177292 56.2474 25
      vertex -0.095459 56.2492 25
    endloop
  endfacet
  facet normal -0.0219907 0.999758 0
    outer loop
      vertex -0.177292 56.2474 25
      vertex -0.095459 56.2492 0
      vertex -0.177292 56.2474 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.75 52.0311 25
      vertex 3.50618 55.1738 25
      vertex 3.43892 55.2187 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.50618 55.1738 25
      vertex 3.19741 50.4236 25
      vertex 3.5 49.8 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.75 52.0311 25
      vertex 3.43892 55.2187 25
      vertex 3.39325 55.2485 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 3.3287 50.0816 25
      vertex 3.40414 49.8 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 3.39325 55.2485 25
      vertex 3.32281 55.2934 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 3.32281 55.2934 25
      vertex 3.27649 55.3222 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 3.27649 55.3222 25
      vertex 3.20728 55.3642 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 3.19741 50.4236 25
      vertex 3.3287 50.0816 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 3.20728 55.3642 25
      vertex 3.16034 55.392 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 3.16034 55.392 25
      vertex 3.08955 55.4328 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 3.08955 55.4328 25
      vertex 3.04204 55.4596 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.50618 55.1738 25
      vertex 3.03109 50.75 25
      vertex 3.19741 50.4236 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 3.04204 55.4596 25
      vertex 2.96996 55.4991 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 2.96996 55.4991 25
      vertex 2.92184 55.5249 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 2.92184 55.5249 25
      vertex 2.84985 55.5623 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.50618 55.1738 25
      vertex 2.83156 51.0572 25
      vertex 3.03109 50.75 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 2.84985 55.5623 25
      vertex 2.80121 55.587 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 2.80121 55.587 25
      vertex 2.72757 55.6233 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.42358 52.1974 25
      vertex 2.72757 55.6233 25
      vertex 2.67839 55.6469 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.67839 55.6469 25
      vertex 2.60434 55.6814 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.50618 55.1738 25
      vertex 2.60101 51.342 25
      vertex 2.83156 51.0572 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.60434 55.6814 25
      vertex 2.55467 55.7039 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.55467 55.7039 25
      vertex 2.47951 55.737 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.47951 55.737 25
      vertex 2.42934 55.7584 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.42934 55.7584 25
      vertex 2.35411 55.7896 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.50618 55.1738 25
      vertex 2.34196 51.601 25
      vertex 2.60101 51.342 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.35411 55.7896 25
      vertex 2.3035 55.8099 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.3035 55.8099 25
      vertex 2.22705 55.8397 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.22705 55.8397 25
      vertex 2.17601 55.8589 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.17601 55.8589 25
      vertex 2.09927 55.8868 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.50618 55.1738 25
      vertex 2.05725 51.8316 25
      vertex 2.34196 51.601 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.09927 55.8868 25
      vertex 2.04782 55.9049 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.08156 52.3287 25
      vertex 2.04782 55.9049 25
      vertex 1.96928 55.9315 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.96928 55.9315 25
      vertex 1.91745 55.9485 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.91745 55.9485 25
      vertex 1.84085 55.9726 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.84085 55.9726 25
      vertex 1.78867 55.9885 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.50618 55.1738 25
      vertex 1.75 52.0311 25
      vertex 2.05725 51.8316 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.78867 55.9885 25
      vertex 1.70967 56.0115 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.70967 56.0115 25
      vertex 1.65714 56.0262 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.65714 56.0262 25
      vertex 1.57776 56.0475 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.57776 56.0475 25
      vertex 1.52493 56.061 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.52493 56.061 25
      vertex 1.44609 56.0803 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.39325 55.2485 25
      vertex 1.42358 52.1974 25
      vertex 1.75 52.0311 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.44609 56.0803 25
      vertex 1.39297 56.0927 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.39297 56.0927 25
      vertex 1.31221 56.1106 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.31221 56.1106 25
      vertex 1.25883 56.1218 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.727691 52.4235 25
      vertex 1.25883 56.1218 25
      vertex 1.17912 56.1377 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 1.17912 56.1377 25
      vertex 1.12552 56.1477 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 2.67839 55.6469 25
      vertex 1.08156 52.3287 25
      vertex 1.42358 52.1974 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 1.12552 56.1477 25
      vertex 1.04567 56.1618 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 1.04567 56.1618 25
      vertex 0.991852 56.1707 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0.991852 56.1707 25
      vertex 0.910187 56.1833 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0.910187 56.1833 25
      vertex 0.856201 56.191 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0.856201 56.191 25
      vertex 0.775299 56.2016 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.96928 55.9315 25
      vertex 0.727691 52.4235 25
      vertex 1.08156 52.3287 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0.775299 56.2016 25
      vertex 0.721146 56.2082 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0.721146 56.2082 25
      vertex 0.639374 56.2171 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0.639374 56.2171 25
      vertex 0.585098 56.2225 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0.585098 56.2225 25
      vertex 0.504288 56.2295 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0.504288 56.2295 25
      vertex 0.449905 56.2337 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0.449905 56.2337 25
      vertex 0.368088 56.2391 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 1.17912 56.1377 25
      vertex 0.365849 52.4808 25
      vertex 0.727691 52.4235 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0 52.5 25
      vertex 0.368088 56.2391 25
      vertex 0.313629 56.242 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0 52.5 25
      vertex 0.313629 56.242 25
      vertex 0.231796 56.2456 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0 52.5 25
      vertex 0.231796 56.2456 25
      vertex 0.177292 56.2474 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0 52.5 25
      vertex 0.177292 56.2474 25
      vertex 0.095459 56.2492 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0 52.5 25
      vertex 0.095459 56.2492 25
      vertex 0.0409241 56.2498 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.368088 56.2391 25
      vertex 0 52.5 25
      vertex 0.365849 52.4808 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.0409241 56.2498 25
      vertex 0 52.5 25
      vertex 0.0409241 56.2498 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.095459 56.2492 25
      vertex 0 52.5 25
      vertex -0.0409241 56.2498 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.177292 56.2474 25
      vertex 0 52.5 25
      vertex -0.095459 56.2492 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.231796 56.2456 25
      vertex 0 52.5 25
      vertex -0.177292 56.2474 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.313629 56.242 25
      vertex 0 52.5 25
      vertex -0.231796 56.2456 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.368088 56.2391 25
      vertex 0 52.5 25
      vertex -0.313629 56.242 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0 52.5 25
      vertex -0.368088 56.2391 25
      vertex -0.365849 52.4808 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.449905 56.2337 25
      vertex -0.365849 52.4808 25
      vertex -0.368088 56.2391 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.504288 56.2295 25
      vertex -0.365849 52.4808 25
      vertex -0.449905 56.2337 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.585098 56.2225 25
      vertex -0.365849 52.4808 25
      vertex -0.504288 56.2295 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.639374 56.2171 25
      vertex -0.365849 52.4808 25
      vertex -0.585098 56.2225 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.721146 56.2082 25
      vertex -0.365849 52.4808 25
      vertex -0.639374 56.2171 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.775299 56.2016 25
      vertex -0.365849 52.4808 25
      vertex -0.721146 56.2082 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.856201 56.191 25
      vertex -0.365849 52.4808 25
      vertex -0.775299 56.2016 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.910187 56.1833 25
      vertex -0.365849 52.4808 25
      vertex -0.856201 56.191 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -0.991852 56.1707 25
      vertex -0.365849 52.4808 25
      vertex -0.910187 56.1833 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.04567 56.1618 25
      vertex -0.365849 52.4808 25
      vertex -0.991852 56.1707 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.12552 56.1477 25
      vertex -0.365849 52.4808 25
      vertex -1.04567 56.1618 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.17912 56.1377 25
      vertex -0.365849 52.4808 25
      vertex -1.12552 56.1477 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -0.365849 52.4808 25
      vertex -1.17912 56.1377 25
      vertex -0.727691 52.4235 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.25883 56.1218 25
      vertex -0.727691 52.4235 25
      vertex -1.17912 56.1377 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.31221 56.1106 25
      vertex -0.727691 52.4235 25
      vertex -1.25883 56.1218 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.39297 56.0927 25
      vertex -0.727691 52.4235 25
      vertex -1.31221 56.1106 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.44609 56.0803 25
      vertex -0.727691 52.4235 25
      vertex -1.39297 56.0927 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.52493 56.061 25
      vertex -0.727691 52.4235 25
      vertex -1.44609 56.0803 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.57776 56.0475 25
      vertex -0.727691 52.4235 25
      vertex -1.52493 56.061 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.65714 56.0262 25
      vertex -0.727691 52.4235 25
      vertex -1.57776 56.0475 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.70967 56.0115 25
      vertex -0.727691 52.4235 25
      vertex -1.65714 56.0262 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.78867 55.9885 25
      vertex -0.727691 52.4235 25
      vertex -1.70967 56.0115 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.84085 55.9726 25
      vertex -0.727691 52.4235 25
      vertex -1.78867 55.9885 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.91745 55.9485 25
      vertex -0.727691 52.4235 25
      vertex -1.84085 55.9726 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -1.96928 55.9315 25
      vertex -0.727691 52.4235 25
      vertex -1.91745 55.9485 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -0.727691 52.4235 25
      vertex -1.96928 55.9315 25
      vertex -1.08156 52.3287 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.04782 55.9049 25
      vertex -1.08156 52.3287 25
      vertex -1.96928 55.9315 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.09927 55.8868 25
      vertex -1.08156 52.3287 25
      vertex -2.04782 55.9049 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.17601 55.8589 25
      vertex -1.08156 52.3287 25
      vertex -2.09927 55.8868 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.22705 55.8397 25
      vertex -1.08156 52.3287 25
      vertex -2.17601 55.8589 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.3035 55.8099 25
      vertex -1.08156 52.3287 25
      vertex -2.22705 55.8397 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.35411 55.7896 25
      vertex -1.08156 52.3287 25
      vertex -2.3035 55.8099 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.42934 55.7584 25
      vertex -1.08156 52.3287 25
      vertex -2.35411 55.7896 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.47951 55.737 25
      vertex -1.08156 52.3287 25
      vertex -2.42934 55.7584 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.55467 55.7039 25
      vertex -1.08156 52.3287 25
      vertex -2.47951 55.737 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.60434 55.6814 25
      vertex -1.08156 52.3287 25
      vertex -2.55467 55.7039 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.67839 55.6469 25
      vertex -1.08156 52.3287 25
      vertex -2.60434 55.6814 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -1.08156 52.3287 25
      vertex -2.67839 55.6469 25
      vertex -1.42358 52.1974 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.72757 55.6233 25
      vertex -1.42358 52.1974 25
      vertex -2.67839 55.6469 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.80121 55.587 25
      vertex -1.42358 52.1974 25
      vertex -2.72757 55.6233 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.84985 55.5623 25
      vertex -1.42358 52.1974 25
      vertex -2.80121 55.587 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.92184 55.5249 25
      vertex -1.42358 52.1974 25
      vertex -2.84985 55.5623 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -2.96996 55.4991 25
      vertex -1.42358 52.1974 25
      vertex -2.92184 55.5249 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.0416 55.4599 25
      vertex -1.42358 52.1974 25
      vertex -2.96996 55.4991 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.08913 55.4331 25
      vertex -1.42358 52.1974 25
      vertex -3.0416 55.4599 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.16081 55.3917 25
      vertex -1.42358 52.1974 25
      vertex -3.08913 55.4331 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.20773 55.3639 25
      vertex -1.42358 52.1974 25
      vertex -3.16081 55.3917 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.27649 55.3222 25
      vertex -1.42358 52.1974 25
      vertex -3.20773 55.3639 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.32281 55.2934 25
      vertex -1.42358 52.1974 25
      vertex -3.27649 55.3222 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.39325 55.2485 25
      vertex -1.42358 52.1974 25
      vertex -3.32281 55.2934 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -1.42358 52.1974 25
      vertex -3.39325 55.2485 25
      vertex -1.75 52.0311 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.43892 55.2187 25
      vertex -1.75 52.0311 25
      vertex -3.39325 55.2485 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.50618 55.1738 25
      vertex -1.75 52.0311 25
      vertex -3.43892 55.2187 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.55119 55.143 25
      vertex -1.75 52.0311 25
      vertex -3.50618 55.1738 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.61794 55.0963 25
      vertex -1.75 52.0311 25
      vertex -3.55119 55.143 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.66228 55.0645 25
      vertex -1.75 52.0311 25
      vertex -3.61794 55.0963 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.7281 55.0162 25
      vertex -1.75 52.0311 25
      vertex -3.66228 55.0645 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -3.77173 54.9835 25
      vertex -1.75 52.0311 25
      vertex -3.7281 55.0162 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -4.073 54.7319 25
      vertex -1.75 52.0311 25
      vertex -3.77173 54.9835 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -1.75 52.0311 25
      vertex -4.073 54.7319 25
      vertex -2.05725 51.8316 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -4.34633 54.4502 25
      vertex -2.05725 51.8316 25
      vertex -4.073 54.7319 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -4.5887 54.1414 25
      vertex -2.05725 51.8316 25
      vertex -4.34633 54.4502 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -2.05725 51.8316 25
      vertex -4.5887 54.1414 25
      vertex -2.34196 51.601 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -4.88516 53.642 25
      vertex -2.34196 51.601 25
      vertex -4.5887 54.1414 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -2.34196 51.601 25
      vertex -4.88516 53.642 25
      vertex -2.60101 51.342 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -6.25 0 25
      vertex -3.5 49.8 25
      vertex -6.25 50 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -2.60101 51.342 25
      vertex -4.88516 53.642 25
      vertex -2.83156 51.0572 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -5.86327 51.6586 25
      vertex -2.83156 51.0572 25
      vertex -4.88516 53.642 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -2.83156 51.0572 25
      vertex -5.86327 51.6586 25
      vertex -3.03109 50.75 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -3.5 49.8 25
      vertex -6.25 0 25
      vertex -3.5 -3.60902 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -3.03109 50.75 25
      vertex -5.86327 51.6586 25
      vertex -3.19741 50.4236 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -6.01822 51.2979 25
      vertex -3.19741 50.4236 25
      vertex -5.86327 51.6586 25
    endloop
  endfacet
  facet normal -0 -0 1
    outer loop
      vertex -4.02527 -3.4258 25
      vertex -3.5 -3.60902 25
      vertex -6.25 0 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -3.3287 50.0816 25
      vertex -3.5 49.8 25
      vertex -3.40414 49.8 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -3.5 -3.60902 25
      vertex -4.02527 -3.4258 25
      vertex -3.65881 -3.56647 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -3.19741 50.4236 25
      vertex -6.01822 51.2979 25
      vertex -3.3287 50.0816 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -4.02527 -3.4258 25
      vertex -6.25 0 25
      vertex -4.375 -3.24759 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -4.375 -3.24759 25
      vertex -6.25 0 25
      vertex -4.70419 -3.03381 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -4.70419 -3.03381 25
      vertex -6.25 0 25
      vertex -5.00925 -2.78679 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -5.28679 -2.50925 25
      vertex -6.25 0 25
      vertex -5.53381 -2.20419 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -3.3287 50.0816 25
      vertex -6.01822 51.2979 25
      vertex -3.5 49.8 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -5.00925 -2.78679 25
      vertex -6.25 0 25
      vertex -5.28679 -2.50925 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -6.13461 50.9231 25
      vertex -3.5 49.8 25
      vertex -6.01822 51.2979 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -5.53381 -2.20419 25
      vertex -6.25 0 25
      vertex -5.74759 -1.875 25
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -6.2112 50.5381 25
      vertex -3.5 49.8 25
      vertex -6.13461 50.9231 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -5.74759 -1.875 25
      vertex -6.25 0 25
      vertex -5.9258 -1.52527 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -3.5 49.8 25
      vertex -6.2112 50.5381 25
      vertex -6.25 50 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -5.9258 -1.52527 25
      vertex -6.25 0 25
      vertex -6.06647 -1.15881 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -6.06647 -1.15881 25
      vertex -6.25 0 25
      vertex -6.16806 -0.779663 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -6.16806 -0.779663 25
      vertex -6.25 0 25
      vertex -6.22946 -0.391983 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 6.25 50 25
      vertex 6.22946 50.392 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 6.25 50 25
      vertex 3.5 49.8 25
      vertex 6.25 0 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 6.22946 50.392 25
      vertex 6.16806 50.7797 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 -3.60902 25
      vertex 6.25 0 25
      vertex 3.5 49.8 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 6.16806 50.7797 25
      vertex 6.06647 51.1588 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 6.25 0 25
      vertex 3.5 -3.60902 25
      vertex 6.22946 -0.391983 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 6.22946 -0.391983 25
      vertex 3.5 -3.60902 25
      vertex 6.16806 -0.779663 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 6.06647 51.1588 25
      vertex 5.86327 51.6586 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 6.16806 -0.779663 25
      vertex 3.5 -3.60902 25
      vertex 6.06647 -1.15881 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 6.06647 -1.15881 25
      vertex 3.5 -3.60902 25
      vertex 5.9258 -1.52527 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 5.9258 -1.52527 25
      vertex 3.5 -3.60902 25
      vertex 5.74759 -1.875 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 5.74759 -1.875 25
      vertex 3.5 -3.60902 25
      vertex 5.53381 -2.20419 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 5.86327 51.6586 25
      vertex 4.88516 53.642 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 5.53381 -2.20419 25
      vertex 3.5 -3.60902 25
      vertex 5.28679 -2.50925 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 4.88516 53.642 25
      vertex 4.69337 53.9845 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 4.69337 53.9845 25
      vertex 4.46683 54.305 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 5.28679 -2.50925 25
      vertex 3.5 -3.60902 25
      vertex 5.00925 -2.78679 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 4.46683 54.305 25
      vertex 4.20802 54.6001 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 5.00925 -2.78679 25
      vertex 3.5 -3.60902 25
      vertex 4.70419 -3.03381 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 4.20802 54.6001 25
      vertex 3.77173 54.9835 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 3.77173 54.9835 25
      vertex 3.7281 55.0162 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 3.7281 55.0162 25
      vertex 3.66228 55.0645 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 4.70419 -3.03381 25
      vertex 3.5 -3.60902 25
      vertex 4.375 -3.24759 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 3.66228 55.0645 25
      vertex 3.61794 55.0963 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 3.61794 55.0963 25
      vertex 3.55119 55.143 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3.5 49.8 25
      vertex 3.55119 55.143 25
      vertex 3.50618 55.1738 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 4.375 -3.24759 25
      vertex 3.5 -3.60902 25
      vertex 4.02527 -3.4258 25
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 4.02527 -3.4258 25
      vertex 3.5 -3.60902 25
      vertex 3.65881 -3.56647 25
    endloop
  endfacet
  facet normal -0.163156 0.9866 0
    outer loop
      vertex -0.991852 56.1707 0
      vertex -1.04567 56.1618 25
      vertex -0.991852 56.1707 25
    endloop
  endfacet
  facet normal -0.163156 0.9866 0
    outer loop
      vertex -1.04567 56.1618 25
      vertex -0.991852 56.1707 0
      vertex -1.04567 56.1618 0
    endloop
  endfacet
  facet normal 0.258802 -0.96593 0
    outer loop
      vertex 3.5 -3.60902 0
      vertex 3.65881 -3.56647 25
      vertex 3.5 -3.60902 25
    endloop
  endfacet
  facet normal 0.258802 -0.96593 0
    outer loop
      vertex 3.65881 -3.56647 25
      vertex 3.5 -3.60902 0
      vertex 3.65881 -3.56647 0
    endloop
  endfacet
  facet normal -0.0531757 0.998585 0
    outer loop
      vertex -0.313629 56.242 0
      vertex -0.368088 56.2391 25
      vertex -0.313629 56.242 25
    endloop
  endfacet
  facet normal -0.0531757 0.998585 0
    outer loop
      vertex -0.368088 56.2391 25
      vertex -0.313629 56.242 0
      vertex -0.368088 56.2391 0
    endloop
  endfacet
  facet normal -0.965927 -0.258814 0
    outer loop
      vertex -6.06647 -1.15881 0
      vertex -6.16806 -0.779663 25
      vertex -6.16806 -0.779663 0
    endloop
  endfacet
  facet normal -0.965927 -0.258814 0
    outer loop
      vertex -6.16806 -0.779663 25
      vertex -6.06647 -1.15881 0
      vertex -6.06647 -1.15881 25
    endloop
  endfacet
  facet normal 0.279533 0.960136 -0
    outer loop
      vertex 1.78867 55.9885 0
      vertex 1.70967 56.0115 25
      vertex 1.78867 55.9885 25
    endloop
  endfacet
  facet normal 0.279533 0.960136 0
    outer loop
      vertex 1.70967 56.0115 25
      vertex 1.78867 55.9885 0
      vertex 1.70967 56.0115 0
    endloop
  endfacet
  facet normal -0.640998 0.767542 0
    outer loop
      vertex -3.77173 54.9835 0
      vertex -4.073 54.7319 25
      vertex -3.77173 54.9835 25
    endloop
  endfacet
  facet normal -0.640998 0.767542 0
    outer loop
      vertex -4.073 54.7319 25
      vertex -3.77173 54.9835 0
      vertex -4.073 54.7319 0
    endloop
  endfacet
  facet normal 0.173891 0.984765 -0
    outer loop
      vertex 1.12552 56.1477 0
      vertex 1.04567 56.1618 25
      vertex 1.12552 56.1477 25
    endloop
  endfacet
  facet normal 0.173891 0.984765 0
    outer loop
      vertex 1.04567 56.1618 25
      vertex 1.12552 56.1477 0
      vertex 1.04567 56.1618 0
    endloop
  endfacet
  facet normal 0.491314 0.870982 -0
    outer loop
      vertex 3.08955 55.4328 0
      vertex 3.04204 55.4596 25
      vertex 3.08955 55.4328 25
    endloop
  endfacet
  facet normal 0.491314 0.870982 0
    outer loop
      vertex 3.04204 55.4596 25
      vertex 3.08955 55.4328 0
      vertex 3.04204 55.4596 0
    endloop
  endfacet
  facet normal -0.537511 0.843257 0
    outer loop
      vertex -3.32281 55.2934 0
      vertex -3.39325 55.2485 25
      vertex -3.32281 55.2934 25
    endloop
  endfacet
  facet normal -0.537511 0.843257 0
    outer loop
      vertex -3.39325 55.2485 25
      vertex -3.32281 55.2934 0
      vertex -3.39325 55.2485 0
    endloop
  endfacet
  facet normal -0.0110015 0.999939 0
    outer loop
      vertex -0.0409241 56.2498 0
      vertex -0.095459 56.2492 25
      vertex -0.0409241 56.2498 25
    endloop
  endfacet
  facet normal -0.0110015 0.999939 0
    outer loop
      vertex -0.095459 56.2492 25
      vertex -0.0409241 56.2498 0
      vertex -0.095459 56.2492 0
    endloop
  endfacet
  facet normal -0.461015 0.887392 0
    outer loop
      vertex -2.84985 55.5623 0
      vertex -2.92184 55.5249 25
      vertex -2.84985 55.5623 25
    endloop
  endfacet
  facet normal -0.461015 0.887392 0
    outer loop
      vertex -2.92184 55.5249 25
      vertex -2.84985 55.5623 0
      vertex -2.92184 55.5249 0
    endloop
  endfacet
  facet normal 0.412628 0.9109 -0
    outer loop
      vertex 2.60434 55.6814 0
      vertex 2.55467 55.7039 25
      vertex 2.60434 55.6814 25
    endloop
  endfacet
  facet normal 0.412628 0.9109 0
    outer loop
      vertex 2.55467 55.7039 25
      vertex 2.60434 55.6814 0
      vertex 2.55467 55.7039 0
    endloop
  endfacet
  facet normal -0.120982 0.992655 0
    outer loop
      vertex -0.721146 56.2082 0
      vertex -0.775299 56.2016 25
      vertex -0.721146 56.2082 25
    endloop
  endfacet
  facet normal -0.120982 0.992655 0
    outer loop
      vertex -0.775299 56.2016 25
      vertex -0.721146 56.2082 0
      vertex -0.775299 56.2016 0
    endloop
  endfacet
  facet normal 0.0330071 0.999455 -0
    outer loop
      vertex 0.231796 56.2456 0
      vertex 0.177292 56.2474 25
      vertex 0.231796 56.2456 25
    endloop
  endfacet
  facet normal 0.0330071 0.999455 0
    outer loop
      vertex 0.177292 56.2474 25
      vertex 0.231796 56.2456 0
      vertex 0.177292 56.2474 0
    endloop
  endfacet
  facet normal -0.546464 0.837483 0
    outer loop
      vertex -3.39325 55.2485 0
      vertex -3.43892 55.2187 25
      vertex -3.39325 55.2485 25
    endloop
  endfacet
  facet normal -0.546464 0.837483 0
    outer loop
      vertex -3.43892 55.2187 25
      vertex -3.39325 55.2485 0
      vertex -3.43892 55.2187 0
    endloop
  endfacet
  facet normal 0.152485 0.988306 -0
    outer loop
      vertex 0.991852 56.1707 0
      vertex 0.910187 56.1833 25
      vertex 0.991852 56.1707 25
    endloop
  endfacet
  facet normal 0.152485 0.988306 0
    outer loop
      vertex 0.910187 56.1833 25
      vertex 0.991852 56.1707 0
      vertex 0.910187 56.1833 0
    endloop
  endfacet
  facet normal -0.383089 0.923711 0
    outer loop
      vertex -2.35411 55.7896 0
      vertex -2.42934 55.7584 25
      vertex -2.35411 55.7896 25
    endloop
  endfacet
  facet normal -0.383089 0.923711 0
    outer loop
      vertex -2.42934 55.7584 25
      vertex -2.35411 55.7896 0
      vertex -2.42934 55.7584 0
    endloop
  endfacet
  facet normal 0.544642 -0.838669 0
    outer loop
      vertex 4.375 -3.24759 0
      vertex 4.70419 -3.03381 25
      vertex 4.375 -3.24759 25
    endloop
  endfacet
  facet normal 0.544642 -0.838669 0
    outer loop
      vertex 4.70419 -3.03381 25
      vertex 4.375 -3.24759 0
      vertex 4.70419 -3.03381 0
    endloop
  endfacet
  facet normal 0.300118 0.953902 -0
    outer loop
      vertex 1.91745 55.9485 0
      vertex 1.84085 55.9726 25
      vertex 1.91745 55.9485 25
    endloop
  endfacet
  facet normal 0.300118 0.953902 0
    outer loop
      vertex 1.84085 55.9726 25
      vertex 1.91745 55.9485 0
      vertex 1.84085 55.9726 0
    endloop
  endfacet
  facet normal 0.987689 -0.156428 0
    outer loop
      vertex 6.16806 -0.779663 25
      vertex 6.22946 -0.391983 0
      vertex 6.22946 -0.391983 25
    endloop
  endfacet
  facet normal 0.987689 -0.156428 0
    outer loop
      vertex 6.22946 -0.391983 0
      vertex 6.16806 -0.779663 25
      vertex 6.16806 -0.779663 0
    endloop
  endfacet
  facet normal 0.965927 -0.258814 0
    outer loop
      vertex 6.06647 -1.15881 25
      vertex 6.16806 -0.779663 0
      vertex 6.16806 -0.779663 25
    endloop
  endfacet
  facet normal 0.965927 -0.258814 0
    outer loop
      vertex 6.16806 -0.779663 0
      vertex 6.06647 -1.15881 25
      vertex 6.06647 -1.15881 0
    endloop
  endfacet
  facet normal -0.152485 0.988306 0
    outer loop
      vertex -0.910187 56.1833 0
      vertex -0.991852 56.1707 25
      vertex -0.910187 56.1833 25
    endloop
  endfacet
  facet normal -0.152485 0.988306 0
    outer loop
      vertex -0.991852 56.1707 25
      vertex -0.910187 56.1833 0
      vertex -0.991852 56.1707 0
    endloop
  endfacet
  facet normal 0.591619 0.806218 -0
    outer loop
      vertex 3.7281 55.0162 0
      vertex 3.66228 55.0645 25
      vertex 3.7281 55.0162 25
    endloop
  endfacet
  facet normal 0.591619 0.806218 0
    outer loop
      vertex 3.66228 55.0645 25
      vertex 3.7281 55.0162 0
      vertex 3.66228 55.0645 0
    endloop
  endfacet
  facet normal -0.331861 0.943328 0
    outer loop
      vertex -2.04782 55.9049 0
      vertex -2.09927 55.8868 25
      vertex -2.04782 55.9049 25
    endloop
  endfacet
  facet normal -0.331861 0.943328 0
    outer loop
      vertex -2.09927 55.8868 25
      vertex -2.04782 55.9049 0
      vertex -2.09927 55.8868 0
    endloop
  endfacet
  facet normal -0.291483 0.956576 0
    outer loop
      vertex -1.78867 55.9885 0
      vertex -1.84085 55.9726 25
      vertex -1.78867 55.9885 25
    endloop
  endfacet
  facet normal -0.291483 0.956576 0
    outer loop
      vertex -1.84085 55.9726 25
      vertex -1.78867 55.9885 0
      vertex -1.84085 55.9726 0
    endloop
  endfacet
  facet normal 0.0990027 0.995087 -0
    outer loop
      vertex 0.639374 56.2171 0
      vertex 0.585098 56.2225 25
      vertex 0.639374 56.2171 25
    endloop
  endfacet
  facet normal 0.0990027 0.995087 0
    outer loop
      vertex 0.585098 56.2225 25
      vertex 0.639374 56.2171 0
      vertex 0.585098 56.2225 0
    endloop
  endfacet
  facet normal 0.442139 0.896946 -0
    outer loop
      vertex 2.80121 55.587 0
      vertex 2.72757 55.6233 25
      vertex 2.80121 55.587 25
    endloop
  endfacet
  facet normal 0.442139 0.896946 0
    outer loop
      vertex 2.72757 55.6233 25
      vertex 2.80121 55.587 0
      vertex 2.72757 55.6233 0
    endloop
  endfacet
  facet normal -0.227322 0.97382 0
    outer loop
      vertex -1.39297 56.0927 0
      vertex -1.44609 56.0803 25
      vertex -1.39297 56.0927 25
    endloop
  endfacet
  facet normal -0.227322 0.97382 0
    outer loop
      vertex -1.44609 56.0803 25
      vertex -1.39297 56.0927 0
      vertex -1.44609 56.0803 0
    endloop
  endfacet
  facet normal -0.300118 0.953902 0
    outer loop
      vertex -1.84085 55.9726 0
      vertex -1.91745 55.9485 25
      vertex -1.84085 55.9726 25
    endloop
  endfacet
  facet normal -0.300118 0.953902 0
    outer loop
      vertex -1.91745 55.9485 25
      vertex -1.84085 55.9726 0
      vertex -1.91745 55.9485 0
    endloop
  endfacet
  facet normal 0.163156 0.9866 -0
    outer loop
      vertex 1.04567 56.1618 0
      vertex 0.991852 56.1707 25
      vertex 1.04567 56.1618 25
    endloop
  endfacet
  facet normal 0.163156 0.9866 0
    outer loop
      vertex 0.991852 56.1707 25
      vertex 1.04567 56.1618 0
      vertex 0.991852 56.1707 0
    endloop
  endfacet
  facet normal 0.141201 0.989981 -0
    outer loop
      vertex 0.910187 56.1833 0
      vertex 0.856201 56.191 25
      vertex 0.910187 56.1833 25
    endloop
  endfacet
  facet normal 0.141201 0.989981 0
    outer loop
      vertex 0.856201 56.191 25
      vertex 0.910187 56.1833 0
      vertex 0.856201 56.191 0
    endloop
  endfacet
  facet normal -0.352088 0.935967 0
    outer loop
      vertex -2.17601 55.8589 0
      vertex -2.22705 55.8397 25
      vertex -2.17601 55.8589 25
    endloop
  endfacet
  facet normal -0.352088 0.935967 0
    outer loop
      vertex -2.22705 55.8397 25
      vertex -2.17601 55.8589 0
      vertex -2.22705 55.8397 0
    endloop
  endfacet
  facet normal 0.291483 0.956576 -0
    outer loop
      vertex 1.84085 55.9726 0
      vertex 1.78867 55.9885 25
      vertex 1.84085 55.9726 25
    endloop
  endfacet
  facet normal 0.291483 0.956576 0
    outer loop
      vertex 1.78867 55.9885 25
      vertex 1.84085 55.9726 0
      vertex 1.78867 55.9885 0
    endloop
  endfacet
  facet normal 0.0770007 0.997031 -0
    outer loop
      vertex 0.504288 56.2295 0
      vertex 0.449905 56.2337 25
      vertex 0.504288 56.2295 25
    endloop
  endfacet
  facet normal 0.0770007 0.997031 0
    outer loop
      vertex 0.449905 56.2337 25
      vertex 0.504288 56.2295 0
      vertex 0.449905 56.2337 0
    endloop
  endfacet
  facet normal 0.403041 0.915182 -0
    outer loop
      vertex 2.55467 55.7039 0
      vertex 2.47951 55.737 25
      vertex 2.55467 55.7039 25
    endloop
  endfacet
  facet normal 0.403041 0.915182 0
    outer loop
      vertex 2.47951 55.737 25
      vertex 2.55467 55.7039 0
      vertex 2.47951 55.737 0
    endloop
  endfacet
  facet normal -0.216393 0.976306 0
    outer loop
      vertex -1.31221 56.1106 0
      vertex -1.39297 56.0927 25
      vertex -1.31221 56.1106 25
    endloop
  endfacet
  facet normal -0.216393 0.976306 0
    outer loop
      vertex -1.39297 56.0927 25
      vertex -1.31221 56.1106 0
      vertex -1.39297 56.0927 0
    endloop
  endfacet
  facet normal 0.120982 0.992655 -0
    outer loop
      vertex 0.775299 56.2016 0
      vertex 0.721146 56.2082 25
      vertex 0.775299 56.2016 25
    endloop
  endfacet
  facet normal 0.120982 0.992655 0
    outer loop
      vertex 0.721146 56.2082 25
      vertex 0.775299 56.2016 0
      vertex 0.721146 56.2082 0
    endloop
  endfacet
  facet normal 0.195619 0.98068 -0
    outer loop
      vertex 1.25883 56.1218 0
      vertex 1.17912 56.1377 25
      vertex 1.25883 56.1218 25
    endloop
  endfacet
  facet normal 0.195619 0.98068 0
    outer loop
      vertex 1.17912 56.1377 25
      vertex 1.25883 56.1218 0
      vertex 1.17912 56.1377 0
    endloop
  endfacet
  facet normal 0.0110015 0.999939 -0
    outer loop
      vertex 0.095459 56.2492 0
      vertex 0.0409241 56.2498 25
      vertex 0.095459 56.2492 25
    endloop
  endfacet
  facet normal 0.0110015 0.999939 0
    outer loop
      vertex 0.0409241 56.2498 25
      vertex 0.095459 56.2492 0
      vertex 0.0409241 56.2498 0
    endloop
  endfacet
  facet normal 0.0658577 0.997829 -0
    outer loop
      vertex 0.449905 56.2337 0
      vertex 0.368088 56.2391 25
      vertex 0.449905 56.2337 25
    endloop
  endfacet
  facet normal 0.0658577 0.997829 0
    outer loop
      vertex 0.368088 56.2391 25
      vertex 0.449905 56.2337 0
      vertex 0.368088 56.2391 0
    endloop
  endfacet
  facet normal 0.472526 0.881317 -0
    outer loop
      vertex 2.96996 55.4991 0
      vertex 2.92184 55.5249 25
      vertex 2.96996 55.4991 25
    endloop
  endfacet
  facet normal 0.472526 0.881317 0
    outer loop
      vertex 2.92184 55.5249 25
      vertex 2.96996 55.4991 0
      vertex 2.92184 55.5249 0
    endloop
  endfacet
  facet normal -0.509742 0.860327 0
    outer loop
      vertex -3.16081 55.3917 0
      vertex -3.20773 55.3639 25
      vertex -3.16081 55.3917 25
    endloop
  endfacet
  facet normal -0.509742 0.860327 0
    outer loop
      vertex -3.20773 55.3639 25
      vertex -3.16081 55.3917 0
      vertex -3.20773 55.3639 0
    endloop
  endfacet
  facet normal 0.0862998 0.996269 -0
    outer loop
      vertex 0.585098 56.2225 0
      vertex 0.504288 56.2295 25
      vertex 0.585098 56.2225 25
    endloop
  endfacet
  facet normal 0.0862998 0.996269 0
    outer loop
      vertex 0.504288 56.2295 25
      vertex 0.585098 56.2225 0
      vertex 0.504288 56.2295 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -3.5 49.8 0
      vertex -3.5 -3.60902 0
    endloop
  endfacet
  facet normal 0 -0 -1
    outer loop
      vertex -6.2112 50.5381 0
      vertex -3.5 49.8 0
      vertex -6.25 50 0
    endloop
  endfacet
  facet normal 0 -0 -1
    outer loop
      vertex -4.88516 53.642 0
      vertex -3.5 49.8 0
      vertex -5.86327 51.6586 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -4.02527 -3.4258 0
      vertex -3.5 -3.60902 0
      vertex -3.65881 -3.56647 0
    endloop
  endfacet
  facet normal 0 -0 -1
    outer loop
      vertex -4.5887 54.1414 0
      vertex -3.5 49.8 0
      vertex -4.88516 53.642 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -3.55119 55.143 0
      vertex -3.50618 55.1738 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -3.66228 55.0645 0
      vertex -3.61794 55.0963 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 -3.60902 0
      vertex -4.02527 -3.4258 0
      vertex -6.25 0 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -3.7281 55.0162 0
      vertex -3.66228 55.0645 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -3.77173 54.9835 0
      vertex -3.7281 55.0162 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -4.02527 -3.4258 0
      vertex -4.375 -3.24759 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -4.073 54.7319 0
      vertex -3.77173 54.9835 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -4.375 -3.24759 0
      vertex -4.70419 -3.03381 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -4.34633 54.4502 0
      vertex -4.073 54.7319 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -4.70419 -3.03381 0
      vertex -5.00925 -2.78679 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -5.00925 -2.78679 0
      vertex -5.28679 -2.50925 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -5.28679 -2.50925 0
      vertex -5.53381 -2.20419 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -5.53381 -2.20419 0
      vertex -5.74759 -1.875 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -6.25 0 0
      vertex -6.25 50 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -5.74759 -1.875 0
      vertex -5.9258 -1.52527 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -4.5887 54.1414 0
      vertex -4.34633 54.4502 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -5.9258 -1.52527 0
      vertex -6.06647 -1.15881 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -3.61794 55.0963 0
      vertex -3.55119 55.143 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -6.06647 -1.15881 0
      vertex -6.16806 -0.779663 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -6.01822 51.2979 0
      vertex -5.86327 51.6586 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -6.25 0 0
      vertex -6.16806 -0.779663 0
      vertex -6.22946 -0.391983 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -6.13461 50.9231 0
      vertex -6.01822 51.2979 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -6.2112 50.5381 0
      vertex -6.13461 50.9231 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 6.25 0 0
      vertex 6.22946 -0.391983 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 6.25 0 0
      vertex 3.5 49.8 0
      vertex 6.25 50 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 6.22946 -0.391983 0
      vertex 6.16806 -0.779663 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 6.25 50 0
      vertex 3.5 49.8 0
      vertex 6.22946 50.392 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 6.16806 -0.779663 0
      vertex 6.06647 -1.15881 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 6.22946 50.392 0
      vertex 3.5 49.8 0
      vertex 6.16806 50.7797 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 6.06647 -1.15881 0
      vertex 5.9258 -1.52527 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 6.16806 50.7797 0
      vertex 3.5 49.8 0
      vertex 6.06647 51.1588 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 5.9258 -1.52527 0
      vertex 5.74759 -1.875 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 5.74759 -1.875 0
      vertex 5.53381 -2.20419 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 5.53381 -2.20419 0
      vertex 5.28679 -2.50925 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 5.28679 -2.50925 0
      vertex 5.00925 -2.78679 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.3287 50.0816 0
      vertex 6.06647 51.1588 0
      vertex 3.5 49.8 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 5.00925 -2.78679 0
      vertex 4.70419 -3.03381 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.19741 50.4236 0
      vertex 6.06647 51.1588 0
      vertex 3.3287 50.0816 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.03109 50.75 0
      vertex 5.86327 51.6586 0
      vertex 3.19741 50.4236 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 4.70419 -3.03381 0
      vertex 4.375 -3.24759 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 2.83156 51.0572 0
      vertex 5.86327 51.6586 0
      vertex 3.03109 50.75 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 4.375 -3.24759 0
      vertex 4.02527 -3.4258 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 5.86327 51.6586 0
      vertex 2.83156 51.0572 0
      vertex 4.88516 53.642 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 2.60101 51.342 0
      vertex 4.88516 53.642 0
      vertex 2.83156 51.0572 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 2.34196 51.601 0
      vertex 4.88516 53.642 0
      vertex 2.60101 51.342 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.5 -3.60902 0
      vertex 4.02527 -3.4258 0
      vertex 3.65881 -3.56647 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 4.88516 53.642 0
      vertex 2.34196 51.601 0
      vertex 4.69337 53.9845 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 2.05725 51.8316 0
      vertex 4.69337 53.9845 0
      vertex 2.34196 51.601 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 4.69337 53.9845 0
      vertex 2.05725 51.8316 0
      vertex 4.46683 54.305 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 6.25 0 0
      vertex 3.5 -3.60902 0
      vertex 3.5 49.8 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 4.46683 54.305 0
      vertex 2.05725 51.8316 0
      vertex 4.20802 54.6001 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 1.75 52.0311 0
      vertex 4.20802 54.6001 0
      vertex 2.05725 51.8316 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.3287 50.0816 0
      vertex 3.5 49.8 0
      vertex 3.40414 49.8 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 6.06647 51.1588 0
      vertex 3.19741 50.4236 0
      vertex 5.86327 51.6586 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 4.20802 54.6001 0
      vertex 1.75 52.0311 0
      vertex 3.77173 54.9835 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.77173 54.9835 0
      vertex 1.75 52.0311 0
      vertex 3.7281 55.0162 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.7281 55.0162 0
      vertex 1.75 52.0311 0
      vertex 3.66228 55.0645 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.66228 55.0645 0
      vertex 1.75 52.0311 0
      vertex 3.61794 55.0963 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.61794 55.0963 0
      vertex 1.75 52.0311 0
      vertex 3.55119 55.143 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.55119 55.143 0
      vertex 1.75 52.0311 0
      vertex 3.50618 55.1738 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.50618 55.1738 0
      vertex 1.75 52.0311 0
      vertex 3.43892 55.2187 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.43892 55.2187 0
      vertex 1.75 52.0311 0
      vertex 3.39325 55.2485 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 1.42358 52.1974 0
      vertex 3.39325 55.2485 0
      vertex 1.75 52.0311 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.39325 55.2485 0
      vertex 1.42358 52.1974 0
      vertex 3.32281 55.2934 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.32281 55.2934 0
      vertex 1.42358 52.1974 0
      vertex 3.27649 55.3222 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.27649 55.3222 0
      vertex 1.42358 52.1974 0
      vertex 3.20728 55.3642 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.20728 55.3642 0
      vertex 1.42358 52.1974 0
      vertex 3.16034 55.392 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.16034 55.392 0
      vertex 1.42358 52.1974 0
      vertex 3.08955 55.4328 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.08955 55.4328 0
      vertex 1.42358 52.1974 0
      vertex 3.04204 55.4596 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 3.04204 55.4596 0
      vertex 1.42358 52.1974 0
      vertex 2.96996 55.4991 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.96996 55.4991 0
      vertex 1.42358 52.1974 0
      vertex 2.92184 55.5249 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.92184 55.5249 0
      vertex 1.42358 52.1974 0
      vertex 2.84985 55.5623 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.84985 55.5623 0
      vertex 1.42358 52.1974 0
      vertex 2.80121 55.587 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.80121 55.587 0
      vertex 1.42358 52.1974 0
      vertex 2.72757 55.6233 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.72757 55.6233 0
      vertex 1.42358 52.1974 0
      vertex 2.67839 55.6469 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 1.08156 52.3287 0
      vertex 2.67839 55.6469 0
      vertex 1.42358 52.1974 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.67839 55.6469 0
      vertex 1.08156 52.3287 0
      vertex 2.60434 55.6814 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.60434 55.6814 0
      vertex 1.08156 52.3287 0
      vertex 2.55467 55.7039 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.55467 55.7039 0
      vertex 1.08156 52.3287 0
      vertex 2.47951 55.737 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.47951 55.737 0
      vertex 1.08156 52.3287 0
      vertex 2.42934 55.7584 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.42934 55.7584 0
      vertex 1.08156 52.3287 0
      vertex 2.35411 55.7896 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.35411 55.7896 0
      vertex 1.08156 52.3287 0
      vertex 2.3035 55.8099 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.3035 55.8099 0
      vertex 1.08156 52.3287 0
      vertex 2.22705 55.8397 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.22705 55.8397 0
      vertex 1.08156 52.3287 0
      vertex 2.17601 55.8589 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.17601 55.8589 0
      vertex 1.08156 52.3287 0
      vertex 2.09927 55.8868 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.09927 55.8868 0
      vertex 1.08156 52.3287 0
      vertex 2.04782 55.9049 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 2.04782 55.9049 0
      vertex 1.08156 52.3287 0
      vertex 1.96928 55.9315 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0.727691 52.4235 0
      vertex 1.96928 55.9315 0
      vertex 1.08156 52.3287 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.96928 55.9315 0
      vertex 0.727691 52.4235 0
      vertex 1.91745 55.9485 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.91745 55.9485 0
      vertex 0.727691 52.4235 0
      vertex 1.84085 55.9726 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.84085 55.9726 0
      vertex 0.727691 52.4235 0
      vertex 1.78867 55.9885 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.78867 55.9885 0
      vertex 0.727691 52.4235 0
      vertex 1.70967 56.0115 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.70967 56.0115 0
      vertex 0.727691 52.4235 0
      vertex 1.65714 56.0262 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.65714 56.0262 0
      vertex 0.727691 52.4235 0
      vertex 1.57776 56.0475 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.57776 56.0475 0
      vertex 0.727691 52.4235 0
      vertex 1.52493 56.061 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.52493 56.061 0
      vertex 0.727691 52.4235 0
      vertex 1.44609 56.0803 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.44609 56.0803 0
      vertex 0.727691 52.4235 0
      vertex 1.39297 56.0927 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.39297 56.0927 0
      vertex 0.727691 52.4235 0
      vertex 1.31221 56.1106 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.31221 56.1106 0
      vertex 0.727691 52.4235 0
      vertex 1.25883 56.1218 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.25883 56.1218 0
      vertex 0.727691 52.4235 0
      vertex 1.17912 56.1377 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0.365849 52.4808 0
      vertex 1.17912 56.1377 0
      vertex 0.727691 52.4235 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.17912 56.1377 0
      vertex 0.365849 52.4808 0
      vertex 1.12552 56.1477 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.12552 56.1477 0
      vertex 0.365849 52.4808 0
      vertex 1.04567 56.1618 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 1.04567 56.1618 0
      vertex 0.365849 52.4808 0
      vertex 0.991852 56.1707 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.991852 56.1707 0
      vertex 0.365849 52.4808 0
      vertex 0.910187 56.1833 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.910187 56.1833 0
      vertex 0.365849 52.4808 0
      vertex 0.856201 56.191 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.856201 56.191 0
      vertex 0.365849 52.4808 0
      vertex 0.775299 56.2016 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.775299 56.2016 0
      vertex 0.365849 52.4808 0
      vertex 0.721146 56.2082 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.721146 56.2082 0
      vertex 0.365849 52.4808 0
      vertex 0.639374 56.2171 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.639374 56.2171 0
      vertex 0.365849 52.4808 0
      vertex 0.585098 56.2225 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.585098 56.2225 0
      vertex 0.365849 52.4808 0
      vertex 0.504288 56.2295 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.504288 56.2295 0
      vertex 0.365849 52.4808 0
      vertex 0.449905 56.2337 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.449905 56.2337 0
      vertex 0.365849 52.4808 0
      vertex 0.368088 56.2391 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0 52.5 0
      vertex 0.368088 56.2391 0
      vertex 0.365849 52.4808 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.368088 56.2391 0
      vertex 0 52.5 0
      vertex 0.313629 56.242 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.313629 56.242 0
      vertex 0 52.5 0
      vertex 0.231796 56.2456 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.231796 56.2456 0
      vertex 0 52.5 0
      vertex 0.177292 56.2474 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.177292 56.2474 0
      vertex 0 52.5 0
      vertex 0.095459 56.2492 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex 0.095459 56.2492 0
      vertex 0 52.5 0
      vertex 0.0409241 56.2498 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0 52.5 0
      vertex -0.0409241 56.2498 0
      vertex 0.0409241 56.2498 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0 52.5 0
      vertex -0.095459 56.2492 0
      vertex -0.0409241 56.2498 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0 52.5 0
      vertex -0.177292 56.2474 0
      vertex -0.095459 56.2492 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0 52.5 0
      vertex -0.231796 56.2456 0
      vertex -0.177292 56.2474 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0 52.5 0
      vertex -0.313629 56.242 0
      vertex -0.231796 56.2456 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.368088 56.2391 0
      vertex 0 52.5 0
      vertex -0.365849 52.4808 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0 52.5 0
      vertex -0.368088 56.2391 0
      vertex -0.313629 56.242 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -0.449905 56.2337 0
      vertex -0.368088 56.2391 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -0.504288 56.2295 0
      vertex -0.449905 56.2337 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -0.585098 56.2225 0
      vertex -0.504288 56.2295 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -0.639374 56.2171 0
      vertex -0.585098 56.2225 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -0.721146 56.2082 0
      vertex -0.639374 56.2171 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.17912 56.1377 0
      vertex -0.365849 52.4808 0
      vertex -0.727691 52.4235 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -0.775299 56.2016 0
      vertex -0.721146 56.2082 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -0.856201 56.191 0
      vertex -0.775299 56.2016 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -0.910187 56.1833 0
      vertex -0.856201 56.191 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -0.991852 56.1707 0
      vertex -0.910187 56.1833 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -1.04567 56.1618 0
      vertex -0.991852 56.1707 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.96928 55.9315 0
      vertex -0.727691 52.4235 0
      vertex -1.08156 52.3287 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -1.12552 56.1477 0
      vertex -1.04567 56.1618 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.365849 52.4808 0
      vertex -1.17912 56.1377 0
      vertex -1.12552 56.1477 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.25883 56.1218 0
      vertex -1.17912 56.1377 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.31221 56.1106 0
      vertex -1.25883 56.1218 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.39297 56.0927 0
      vertex -1.31221 56.1106 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -2.67839 55.6469 0
      vertex -1.08156 52.3287 0
      vertex -1.42358 52.1974 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.44609 56.0803 0
      vertex -1.39297 56.0927 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.52493 56.061 0
      vertex -1.44609 56.0803 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.57776 56.0475 0
      vertex -1.52493 56.061 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.65714 56.0262 0
      vertex -1.57776 56.0475 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.70967 56.0115 0
      vertex -1.65714 56.0262 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.39325 55.2485 0
      vertex -1.42358 52.1974 0
      vertex -1.75 52.0311 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.78867 55.9885 0
      vertex -1.70967 56.0115 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.84085 55.9726 0
      vertex -1.78867 55.9885 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.91745 55.9485 0
      vertex -1.84085 55.9726 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.727691 52.4235 0
      vertex -1.96928 55.9315 0
      vertex -1.91745 55.9485 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.04782 55.9049 0
      vertex -1.96928 55.9315 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.50618 55.1738 0
      vertex -1.75 52.0311 0
      vertex -2.05725 51.8316 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.09927 55.8868 0
      vertex -2.04782 55.9049 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.17601 55.8589 0
      vertex -2.09927 55.8868 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.22705 55.8397 0
      vertex -2.17601 55.8589 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.3035 55.8099 0
      vertex -2.22705 55.8397 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.50618 55.1738 0
      vertex -2.05725 51.8316 0
      vertex -2.34196 51.601 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.35411 55.7896 0
      vertex -2.3035 55.8099 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.42934 55.7584 0
      vertex -2.35411 55.7896 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.47951 55.737 0
      vertex -2.42934 55.7584 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.55467 55.7039 0
      vertex -2.47951 55.737 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.50618 55.1738 0
      vertex -2.34196 51.601 0
      vertex -2.60101 51.342 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.60434 55.6814 0
      vertex -2.55467 55.7039 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.08156 52.3287 0
      vertex -2.67839 55.6469 0
      vertex -2.60434 55.6814 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -2.72757 55.6233 0
      vertex -2.67839 55.6469 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -2.80121 55.587 0
      vertex -2.72757 55.6233 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.50618 55.1738 0
      vertex -2.60101 51.342 0
      vertex -2.83156 51.0572 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -2.84985 55.5623 0
      vertex -2.80121 55.587 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -2.92184 55.5249 0
      vertex -2.84985 55.5623 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -2.96996 55.4991 0
      vertex -2.92184 55.5249 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.50618 55.1738 0
      vertex -2.83156 51.0572 0
      vertex -3.03109 50.75 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -3.0416 55.4599 0
      vertex -2.96996 55.4991 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -3.08913 55.4331 0
      vertex -3.0416 55.4599 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -3.16081 55.3917 0
      vertex -3.08913 55.4331 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.50618 55.1738 0
      vertex -3.03109 50.75 0
      vertex -3.19741 50.4236 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -3.20773 55.3639 0
      vertex -3.16081 55.3917 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -3.27649 55.3222 0
      vertex -3.20773 55.3639 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -3.32281 55.2934 0
      vertex -3.27649 55.3222 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -3.19741 50.4236 0
      vertex -3.3287 50.0816 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.42358 52.1974 0
      vertex -3.39325 55.2485 0
      vertex -3.32281 55.2934 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -3.5 49.8 0
      vertex -3.3287 50.0816 0
      vertex -3.40414 49.8 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.75 52.0311 0
      vertex -3.43892 55.2187 0
      vertex -3.39325 55.2485 0
    endloop
  endfacet
  facet normal -0 0 -1
    outer loop
      vertex -3.19741 50.4236 0
      vertex -3.5 49.8 0
      vertex -3.50618 55.1738 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -1.75 52.0311 0
      vertex -3.50618 55.1738 0
      vertex -3.43892 55.2187 0
    endloop
  endfacet
  facet normal 0.480573 0.876955 -0
    outer loop
      vertex 3.04204 55.4596 0
      vertex 2.96996 55.4991 25
      vertex 3.04204 55.4596 25
    endloop
  endfacet
  facet normal 0.480573 0.876955 0
    outer loop
      vertex 2.96996 55.4991 25
      vertex 3.04204 55.4596 0
      vertex 2.96996 55.4991 0
    endloop
  endfacet
  facet normal 0.461015 0.887392 -0
    outer loop
      vertex 2.92184 55.5249 0
      vertex 2.84985 55.5623 25
      vertex 2.92184 55.5249 25
    endloop
  endfacet
  facet normal 0.461015 0.887392 0
    outer loop
      vertex 2.84985 55.5623 25
      vertex 2.92184 55.5249 0
      vertex 2.84985 55.5623 0
    endloop
  endfacet
  facet normal -0.269487 0.963004 0
    outer loop
      vertex -1.65714 56.0262 0
      vertex -1.70967 56.0115 25
      vertex -1.65714 56.0262 25
    endloop
  endfacet
  facet normal -0.269487 0.963004 0
    outer loop
      vertex -1.70967 56.0115 25
      vertex -1.65714 56.0262 0
      vertex -1.70967 56.0115 0
    endloop
  endfacet
  facet normal 0.422316 0.906449 -0
    outer loop
      vertex 2.67839 55.6469 0
      vertex 2.60434 55.6814 25
      vertex 2.67839 55.6469 25
    endloop
  endfacet
  facet normal 0.422316 0.906449 0
    outer loop
      vertex 2.60434 55.6814 25
      vertex 2.67839 55.6469 0
      vertex 2.60434 55.6814 0
    endloop
  endfacet
  facet normal -0.392348 0.919817 0
    outer loop
      vertex -2.42934 55.7584 0
      vertex -2.47951 55.737 25
      vertex -2.42934 55.7584 25
    endloop
  endfacet
  facet normal -0.392348 0.919817 0
    outer loop
      vertex -2.47951 55.737 25
      vertex -2.42934 55.7584 0
      vertex -2.47951 55.737 0
    endloop
  endfacet
  facet normal -0.555214 0.831708 0
    outer loop
      vertex -3.43892 55.2187 0
      vertex -3.50618 55.1738 25
      vertex -3.43892 55.2187 25
    endloop
  endfacet
  facet normal -0.555214 0.831708 0
    outer loop
      vertex -3.50618 55.1738 25
      vertex -3.43892 55.2187 0
      vertex -3.50618 55.1738 0
    endloop
  endfacet
  facet normal 0.1082 0.994129 -0
    outer loop
      vertex 0.721146 56.2082 0
      vertex 0.639374 56.2171 25
      vertex 0.721146 56.2082 25
    endloop
  endfacet
  facet normal 0.1082 0.994129 0
    outer loop
      vertex 0.639374 56.2171 25
      vertex 0.721146 56.2082 0
      vertex 0.639374 56.2171 0
    endloop
  endfacet
  facet normal -0.237779 0.971319 0
    outer loop
      vertex -1.44609 56.0803 0
      vertex -1.52493 56.061 25
      vertex -1.44609 56.0803 25
    endloop
  endfacet
  facet normal -0.237779 0.971319 0
    outer loop
      vertex -1.52493 56.061 25
      vertex -1.44609 56.0803 0
      vertex -1.52493 56.061 0
    endloop
  endfacet
  facet normal 0.352088 0.935967 -0
    outer loop
      vertex 2.22705 55.8397 0
      vertex 2.17601 55.8589 25
      vertex 2.22705 55.8397 25
    endloop
  endfacet
  facet normal 0.352088 0.935967 0
    outer loop
      vertex 2.17601 55.8589 25
      vertex 2.22705 55.8397 0
      vertex 2.17601 55.8589 0
    endloop
  endfacet
  facet normal -0.472526 0.881317 0
    outer loop
      vertex -2.92184 55.5249 0
      vertex -2.96996 55.4991 25
      vertex -2.92184 55.5249 25
    endloop
  endfacet
  facet normal -0.472526 0.881317 0
    outer loop
      vertex -2.96996 55.4991 25
      vertex -2.92184 55.5249 0
      vertex -2.96996 55.4991 0
    endloop
  endfacet
  facet normal 0.518794 0.854899 -0
    outer loop
      vertex 3.27649 55.3222 0
      vertex 3.20728 55.3642 25
      vertex 3.27649 55.3222 25
    endloop
  endfacet
  facet normal 0.518794 0.854899 0
    outer loop
      vertex 3.20728 55.3642 25
      vertex 3.27649 55.3222 0
      vertex 3.20728 55.3642 0
    endloop
  endfacet
  facet normal 0.432636 0.901569 -0
    outer loop
      vertex 2.72757 55.6233 0
      vertex 2.67839 55.6469 25
      vertex 2.72757 55.6233 25
    endloop
  endfacet
  facet normal 0.432636 0.901569 0
    outer loop
      vertex 2.67839 55.6469 25
      vertex 2.72757 55.6233 0
      vertex 2.67839 55.6469 0
    endloop
  endfacet
  facet normal 0.555214 0.831708 -0
    outer loop
      vertex 3.50618 55.1738 0
      vertex 3.43892 55.2187 25
      vertex 3.50618 55.1738 25
    endloop
  endfacet
  facet normal 0.555214 0.831708 0
    outer loop
      vertex 3.43892 55.2187 25
      vertex 3.50618 55.1738 0
      vertex 3.43892 55.2187 0
    endloop
  endfacet
  facet normal 0.599736 0.800198 -0
    outer loop
      vertex 3.77173 54.9835 0
      vertex 3.7281 55.0162 25
      vertex 3.77173 54.9835 25
    endloop
  endfacet
  facet normal 0.599736 0.800198 0
    outer loop
      vertex 3.7281 55.0162 25
      vertex 3.77173 54.9835 0
      vertex 3.7281 55.0162 0
    endloop
  endfacet
  facet normal 0.890992 -0.454018 0
    outer loop
      vertex 5.74759 -1.875 25
      vertex 5.9258 -1.52527 0
      vertex 5.9258 -1.52527 25
    endloop
  endfacet
  facet normal 0.890992 -0.454018 0
    outer loop
      vertex 5.9258 -1.52527 0
      vertex 5.74759 -1.875 25
      vertex 5.74759 -1.875 0
    endloop
  endfacet
  facet normal -0.341684 0.939815 0
    outer loop
      vertex -2.09927 55.8868 0
      vertex -2.17601 55.8589 25
      vertex -2.09927 55.8868 25
    endloop
  endfacet
  facet normal -0.341684 0.939815 0
    outer loop
      vertex -2.17601 55.8589 25
      vertex -2.09927 55.8868 0
      vertex -2.17601 55.8589 0
    endloop
  endfacet
  facet normal -0.56473 0.825276 0
    outer loop
      vertex -3.50618 55.1738 0
      vertex -3.55119 55.143 25
      vertex -3.50618 55.1738 25
    endloop
  endfacet
  facet normal -0.56473 0.825276 0
    outer loop
      vertex -3.55119 55.143 25
      vertex -3.50618 55.1738 0
      vertex -3.55119 55.143 0
    endloop
  endfacet
  facet normal -0.403041 0.915182 0
    outer loop
      vertex -2.47951 55.737 0
      vertex -2.55467 55.7039 25
      vertex -2.47951 55.737 25
    endloop
  endfacet
  facet normal -0.403041 0.915182 0
    outer loop
      vertex -2.55467 55.7039 25
      vertex -2.47951 55.737 0
      vertex -2.55467 55.7039 0
    endloop
  endfacet
  facet normal -0.52802 0.849232 0
    outer loop
      vertex -3.27649 55.3222 0
      vertex -3.32281 55.2934 25
      vertex -3.27649 55.3222 25
    endloop
  endfacet
  facet normal -0.52802 0.849232 0
    outer loop
      vertex -3.32281 55.2934 25
      vertex -3.27649 55.3222 0
      vertex -3.32281 55.2934 0
    endloop
  endfacet
  facet normal -0.500141 0.865944 0
    outer loop
      vertex -3.08913 55.4331 0
      vertex -3.16081 55.3917 25
      vertex -3.08913 55.4331 25
    endloop
  endfacet
  facet normal -0.500141 0.865944 0
    outer loop
      vertex -3.16081 55.3917 25
      vertex -3.08913 55.4331 0
      vertex -3.16081 55.3917 0
    endloop
  endfacet
  facet normal 0.838669 -0.544642 0
    outer loop
      vertex 5.53381 -2.20419 25
      vertex 5.74759 -1.875 0
      vertex 5.74759 -1.875 25
    endloop
  endfacet
  facet normal 0.838669 -0.544642 0
    outer loop
      vertex 5.74759 -1.875 0
      vertex 5.53381 -2.20419 25
      vertex 5.53381 -2.20419 0
    endloop
  endfacet
  facet normal -0.51855 0.855047 0
    outer loop
      vertex -3.20773 55.3639 0
      vertex -3.27649 55.3222 25
      vertex -3.20773 55.3639 25
    endloop
  endfacet
  facet normal -0.51855 0.855047 0
    outer loop
      vertex -3.27649 55.3222 25
      vertex -3.20773 55.3639 0
      vertex -3.27649 55.3222 0
    endloop
  endfacet
  facet normal -0.591619 0.806218 0
    outer loop
      vertex -3.66228 55.0645 0
      vertex -3.7281 55.0162 25
      vertex -3.66228 55.0645 25
    endloop
  endfacet
  facet normal -0.591619 0.806218 0
    outer loop
      vertex -3.7281 55.0162 25
      vertex -3.66228 55.0645 0
      vertex -3.7281 55.0162 0
    endloop
  endfacet
  facet normal -0.205345 0.97869 0
    outer loop
      vertex -1.25883 56.1218 0
      vertex -1.31221 56.1106 25
      vertex -1.25883 56.1218 25
    endloop
  endfacet
  facet normal -0.205345 0.97869 0
    outer loop
      vertex -1.31221 56.1106 25
      vertex -1.25883 56.1218 0
      vertex -1.31221 56.1106 0
    endloop
  endfacet
  facet normal -0.412628 0.9109 0
    outer loop
      vertex -2.55467 55.7039 0
      vertex -2.60434 55.6814 25
      vertex -2.55467 55.7039 25
    endloop
  endfacet
  facet normal -0.412628 0.9109 0
    outer loop
      vertex -2.60434 55.6814 25
      vertex -2.55467 55.7039 0
      vertex -2.60434 55.6814 0
    endloop
  endfacet
  facet normal -0.480019 0.877258 0
    outer loop
      vertex -2.96996 55.4991 0
      vertex -3.0416 55.4599 25
      vertex -2.96996 55.4991 25
    endloop
  endfacet
  facet normal -0.480019 0.877258 0
    outer loop
      vertex -3.0416 55.4599 25
      vertex -2.96996 55.4991 0
      vertex -3.0416 55.4599 0
    endloop
  endfacet
  facet normal 0.52802 0.849232 -0
    outer loop
      vertex 3.32281 55.2934 0
      vertex 3.27649 55.3222 25
      vertex 3.32281 55.2934 25
    endloop
  endfacet
  facet normal 0.52802 0.849232 0
    outer loop
      vertex 3.27649 55.3222 25
      vertex 3.32281 55.2934 0
      vertex 3.27649 55.3222 0
    endloop
  endfacet
  facet normal 0.499352 0.866399 -0
    outer loop
      vertex 3.16034 55.392 0
      vertex 3.08955 55.4328 25
      vertex 3.16034 55.392 25
    endloop
  endfacet
  facet normal 0.499352 0.866399 0
    outer loop
      vertex 3.08955 55.4328 25
      vertex 3.16034 55.392 0
      vertex 3.08955 55.4328 0
    endloop
  endfacet
  facet normal 0.341684 0.939815 -0
    outer loop
      vertex 2.17601 55.8589 0
      vertex 2.09927 55.8868 25
      vertex 2.17601 55.8589 25
    endloop
  endfacet
  facet normal 0.341684 0.939815 0
    outer loop
      vertex 2.09927 55.8868 25
      vertex 2.17601 55.8589 0
      vertex 2.09927 55.8868 0
    endloop
  endfacet
  facet normal 0.183403 0.983038 -0
    outer loop
      vertex 1.17912 56.1377 0
      vertex 1.12552 56.1477 25
      vertex 1.17912 56.1377 25
    endloop
  endfacet
  facet normal 0.183403 0.983038 0
    outer loop
      vertex 1.12552 56.1477 25
      vertex 1.17912 56.1377 0
      vertex 1.12552 56.1477 0
    endloop
  endfacet
  facet normal 0.452778 0.891624 -0
    outer loop
      vertex 2.84985 55.5623 0
      vertex 2.80121 55.587 25
      vertex 2.84985 55.5623 25
    endloop
  endfacet
  facet normal 0.452778 0.891624 0
    outer loop
      vertex 2.80121 55.587 25
      vertex 2.84985 55.5623 0
      vertex 2.80121 55.587 0
    endloop
  endfacet
  facet normal 0.509581 0.860423 -0
    outer loop
      vertex 3.20728 55.3642 0
      vertex 3.16034 55.392 25
      vertex 3.20728 55.3642 25
    endloop
  endfacet
  facet normal 0.509581 0.860423 0
    outer loop
      vertex 3.16034 55.392 25
      vertex 3.20728 55.3642 0
      vertex 3.16034 55.392 0
    endloop
  endfacet
  facet normal -0.573256 0.819376 0
    outer loop
      vertex -3.55119 55.143 0
      vertex -3.61794 55.0963 25
      vertex -3.55119 55.143 25
    endloop
  endfacet
  facet normal -0.573256 0.819376 0
    outer loop
      vertex -3.61794 55.0963 25
      vertex -3.55119 55.143 0
      vertex -3.61794 55.0963 0
    endloop
  endfacet
  facet normal -0.247581 0.968867 0
    outer loop
      vertex -1.52493 56.061 0
      vertex -1.57776 56.0475 25
      vertex -1.52493 56.061 25
    endloop
  endfacet
  facet normal -0.247581 0.968867 0
    outer loop
      vertex -1.57776 56.0475 25
      vertex -1.52493 56.061 0
      vertex -1.57776 56.0475 0
    endloop
  endfacet
  facet normal -0.311659 0.950194 0
    outer loop
      vertex -1.91745 55.9485 0
      vertex -1.96928 55.9315 25
      vertex -1.91745 55.9485 25
    endloop
  endfacet
  facet normal -0.311659 0.950194 0
    outer loop
      vertex -1.96928 55.9315 25
      vertex -1.91745 55.9485 0
      vertex -1.96928 55.9315 0
    endloop
  endfacet
  facet normal 0.537511 0.843257 -0
    outer loop
      vertex 3.39325 55.2485 0
      vertex 3.32281 55.2934 25
      vertex 3.39325 55.2485 25
    endloop
  endfacet
  facet normal 0.537511 0.843257 0
    outer loop
      vertex 3.32281 55.2934 25
      vertex 3.39325 55.2485 0
      vertex 3.32281 55.2934 0
    endloop
  endfacet
  facet normal 0.205345 0.97869 -0
    outer loop
      vertex 1.31221 56.1106 0
      vertex 1.25883 56.1218 25
      vertex 1.31221 56.1106 25
    endloop
  endfacet
  facet normal 0.205345 0.97869 0
    outer loop
      vertex 1.25883 56.1218 25
      vertex 1.31221 56.1106 0
      vertex 1.25883 56.1218 0
    endloop
  endfacet
  facet normal -0.422316 0.906449 0
    outer loop
      vertex -2.60434 55.6814 0
      vertex -2.67839 55.6469 25
      vertex -2.60434 55.6814 25
    endloop
  endfacet
  facet normal -0.422316 0.906449 0
    outer loop
      vertex -2.67839 55.6469 25
      vertex -2.60434 55.6814 0
      vertex -2.67839 55.6469 0
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 3.5 -3.60902 0
      vertex 3.5 49.8 25
      vertex 3.5 49.8 0
    endloop
  endfacet
  facet normal -1 -0 0
    outer loop
      vertex 3.5 49.8 25
      vertex 3.5 -3.60902 0
      vertex 3.5 -3.60902 25
    endloop
  endfacet
  facet normal 1 -0 0
    outer loop
      vertex -3.5 -3.60902 25
      vertex -3.5 49.8 0
      vertex -3.5 49.8 25
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex -3.5 49.8 0
      vertex -3.5 -3.60902 25
      vertex -3.5 -3.60902 0
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 3.40414 49.8 0
      vertex 3.5 49.8 25
      vertex 3.40414 49.8 25
    endloop
  endfacet
  facet normal 0 -1 -0
    outer loop
      vertex 3.5 49.8 25
      vertex 3.40414 49.8 0
      vertex 3.5 49.8 0
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -3.5 49.8 0
      vertex -3.40414 49.8 25
      vertex -3.5 49.8 25
    endloop
  endfacet
  facet normal 0 -1 -0
    outer loop
      vertex -3.40414 49.8 25
      vertex -3.5 49.8 0
      vertex -3.40414 49.8 0
    endloop
  endfacet
  facet normal 0.933573 -0.358388 0
    outer loop
      vertex -3.3287 50.0816 25
      vertex -3.19741 50.4236 0
      vertex -3.19741 50.4236 25
    endloop
  endfacet
  facet normal 0.933573 -0.358388 0
    outer loop
      vertex -3.19741 50.4236 0
      vertex -3.3287 50.0816 25
      vertex -3.3287 50.0816 0
    endloop
  endfacet
  facet normal -0.933573 -0.358388 0
    outer loop
      vertex 3.3287 50.0816 0
      vertex 3.19741 50.4236 25
      vertex 3.19741 50.4236 0
    endloop
  endfacet
  facet normal -0.933573 -0.358388 0
    outer loop
      vertex 3.19741 50.4236 25
      vertex 3.3287 50.0816 0
      vertex 3.3287 50.0816 25
    endloop
  endfacet
  facet normal -0.544581 -0.838709 0
    outer loop
      vertex 1.75 52.0311 0
      vertex 2.05725 51.8316 25
      vertex 1.75 52.0311 25
    endloop
  endfacet
  facet normal -0.544581 -0.838709 -0
    outer loop
      vertex 2.05725 51.8316 25
      vertex 1.75 52.0311 0
      vertex 2.05725 51.8316 0
    endloop
  endfacet
  facet normal 0.707039 -0.707175 0
    outer loop
      vertex -2.60101 51.342 0
      vertex -2.34196 51.601 25
      vertex -2.60101 51.342 25
    endloop
  endfacet
  facet normal 0.707039 -0.707175 0
    outer loop
      vertex -2.34196 51.601 25
      vertex -2.60101 51.342 0
      vertex -2.34196 51.601 0
    endloop
  endfacet
  facet normal 0.777248 -0.629194 0
    outer loop
      vertex -2.83156 51.0572 25
      vertex -2.60101 51.342 0
      vertex -2.60101 51.342 25
    endloop
  endfacet
  facet normal 0.777248 -0.629194 0
    outer loop
      vertex -2.60101 51.342 0
      vertex -2.83156 51.0572 25
      vertex -2.83156 51.0572 0
    endloop
  endfacet
  facet normal 0.629397 -0.777084 0
    outer loop
      vertex -2.34196 51.601 0
      vertex -2.05725 51.8316 25
      vertex -2.34196 51.601 25
    endloop
  endfacet
  facet normal 0.629397 -0.777084 0
    outer loop
      vertex -2.05725 51.8316 25
      vertex -2.34196 51.601 0
      vertex -2.05725 51.8316 0
    endloop
  endfacet
  facet normal 0.965938 -0.258773 0
    outer loop
      vertex -3.40414 49.8 25
      vertex -3.3287 50.0816 0
      vertex -3.3287 50.0816 25
    endloop
  endfacet
  facet normal 0.965938 -0.258773 0
    outer loop
      vertex -3.3287 50.0816 0
      vertex -3.40414 49.8 25
      vertex -3.40414 49.8 0
    endloop
  endfacet
  facet normal -0.890994 -0.454014 0
    outer loop
      vertex 3.19741 50.4236 0
      vertex 3.03109 50.75 25
      vertex 3.03109 50.75 0
    endloop
  endfacet
  facet normal -0.890994 -0.454014 0
    outer loop
      vertex 3.03109 50.75 25
      vertex 3.19741 50.4236 0
      vertex 3.19741 50.4236 25
    endloop
  endfacet
  facet normal 0.358394 -0.933571 0
    outer loop
      vertex -1.42358 52.1974 0
      vertex -1.08156 52.3287 25
      vertex -1.42358 52.1974 25
    endloop
  endfacet
  facet normal 0.358394 -0.933571 0
    outer loop
      vertex -1.08156 52.3287 25
      vertex -1.42358 52.1974 0
      vertex -1.08156 52.3287 0
    endloop
  endfacet
  facet normal 0.544581 -0.838709 0
    outer loop
      vertex -2.05725 51.8316 0
      vertex -1.75 52.0311 25
      vertex -2.05725 51.8316 25
    endloop
  endfacet
  facet normal 0.544581 -0.838709 0
    outer loop
      vertex -1.75 52.0311 25
      vertex -2.05725 51.8316 0
      vertex -1.75 52.0311 0
    endloop
  endfacet
  facet normal 0.838631 -0.5447 0
    outer loop
      vertex -3.03109 50.75 25
      vertex -2.83156 51.0572 0
      vertex -2.83156 51.0572 25
    endloop
  endfacet
  facet normal 0.838631 -0.5447 0
    outer loop
      vertex -2.83156 51.0572 0
      vertex -3.03109 50.75 25
      vertex -3.03109 50.75 0
    endloop
  endfacet
  facet normal 0.890994 -0.454014 0
    outer loop
      vertex -3.19741 50.4236 25
      vertex -3.03109 50.75 0
      vertex -3.03109 50.75 25
    endloop
  endfacet
  facet normal 0.890994 -0.454014 0
    outer loop
      vertex -3.03109 50.75 0
      vertex -3.19741 50.4236 25
      vertex -3.19741 50.4236 0
    endloop
  endfacet
  facet normal -0.156407 -0.987693 0
    outer loop
      vertex 0.365849 52.4808 0
      vertex 0.727691 52.4235 25
      vertex 0.365849 52.4808 25
    endloop
  endfacet
  facet normal -0.156407 -0.987693 -0
    outer loop
      vertex 0.727691 52.4235 25
      vertex 0.365849 52.4808 0
      vertex 0.727691 52.4235 0
    endloop
  endfacet
  facet normal -0.453949 -0.891028 0
    outer loop
      vertex 1.42358 52.1974 0
      vertex 1.75 52.0311 25
      vertex 1.42358 52.1974 25
    endloop
  endfacet
  facet normal -0.453949 -0.891028 -0
    outer loop
      vertex 1.75 52.0311 25
      vertex 1.42358 52.1974 0
      vertex 1.75 52.0311 0
    endloop
  endfacet
  facet normal -0.707039 -0.707175 0
    outer loop
      vertex 2.34196 51.601 0
      vertex 2.60101 51.342 25
      vertex 2.34196 51.601 25
    endloop
  endfacet
  facet normal -0.707039 -0.707175 -0
    outer loop
      vertex 2.60101 51.342 25
      vertex 2.34196 51.601 0
      vertex 2.60101 51.342 0
    endloop
  endfacet
  facet normal -0.965938 -0.258773 0
    outer loop
      vertex 3.40414 49.8 0
      vertex 3.3287 50.0816 25
      vertex 3.3287 50.0816 0
    endloop
  endfacet
  facet normal -0.965938 -0.258773 0
    outer loop
      vertex 3.3287 50.0816 25
      vertex 3.40414 49.8 0
      vertex 3.40414 49.8 25
    endloop
  endfacet
  facet normal 0.0524085 -0.998626 0
    outer loop
      vertex -0.365849 52.4808 0
      vertex 0 52.5 25
      vertex -0.365849 52.4808 25
    endloop
  endfacet
  facet normal 0.0524085 -0.998626 0
    outer loop
      vertex 0 52.5 25
      vertex -0.365849 52.4808 0
      vertex 0 52.5 0
    endloop
  endfacet
  facet normal -0.629397 -0.777084 0
    outer loop
      vertex 2.05725 51.8316 0
      vertex 2.34196 51.601 25
      vertex 2.05725 51.8316 25
    endloop
  endfacet
  facet normal -0.629397 -0.777084 -0
    outer loop
      vertex 2.34196 51.601 25
      vertex 2.05725 51.8316 0
      vertex 2.34196 51.601 0
    endloop
  endfacet
  facet normal -0.0524085 -0.998626 0
    outer loop
      vertex 0 52.5 0
      vertex 0.365849 52.4808 25
      vertex 0 52.5 25
    endloop
  endfacet
  facet normal -0.0524085 -0.998626 -0
    outer loop
      vertex 0.365849 52.4808 25
      vertex 0 52.5 0
      vertex 0.365849 52.4808 0
    endloop
  endfacet
  facet normal -0.777248 -0.629194 0
    outer loop
      vertex 2.83156 51.0572 0
      vertex 2.60101 51.342 25
      vertex 2.60101 51.342 0
    endloop
  endfacet
  facet normal -0.777248 -0.629194 0
    outer loop
      vertex 2.60101 51.342 25
      vertex 2.83156 51.0572 0
      vertex 2.83156 51.0572 25
    endloop
  endfacet
  facet normal -0.838631 -0.5447 0
    outer loop
      vertex 3.03109 50.75 0
      vertex 2.83156 51.0572 25
      vertex 2.83156 51.0572 0
    endloop
  endfacet
  facet normal -0.838631 -0.5447 0
    outer loop
      vertex 2.83156 51.0572 25
      vertex 3.03109 50.75 0
      vertex 3.03109 50.75 25
    endloop
  endfacet
  facet normal -0.358394 -0.933571 0
    outer loop
      vertex 1.08156 52.3287 0
      vertex 1.42358 52.1974 25
      vertex 1.08156 52.3287 25
    endloop
  endfacet
  facet normal -0.358394 -0.933571 -0
    outer loop
      vertex 1.42358 52.1974 25
      vertex 1.08156 52.3287 0
      vertex 1.42358 52.1974 0
    endloop
  endfacet
  facet normal 0.453949 -0.891028 0
    outer loop
      vertex -1.75 52.0311 0
      vertex -1.42358 52.1974 25
      vertex -1.75 52.0311 25
    endloop
  endfacet
  facet normal 0.453949 -0.891028 0
    outer loop
      vertex -1.42358 52.1974 25
      vertex -1.75 52.0311 0
      vertex -1.42358 52.1974 0
    endloop
  endfacet
  facet normal -0.258771 -0.965939 0
    outer loop
      vertex 0.727691 52.4235 0
      vertex 1.08156 52.3287 25
      vertex 0.727691 52.4235 25
    endloop
  endfacet
  facet normal -0.258771 -0.965939 -0
    outer loop
      vertex 1.08156 52.3287 25
      vertex 0.727691 52.4235 0
      vertex 1.08156 52.3287 0
    endloop
  endfacet
  facet normal 0.156407 -0.987693 0
    outer loop
      vertex -0.727691 52.4235 0
      vertex -0.365849 52.4808 25
      vertex -0.727691 52.4235 25
    endloop
  endfacet
  facet normal 0.156407 -0.987693 0
    outer loop
      vertex -0.365849 52.4808 25
      vertex -0.727691 52.4235 0
      vertex -0.365849 52.4808 0
    endloop
  endfacet
  facet normal 0.258771 -0.965939 0
    outer loop
      vertex -1.08156 52.3287 0
      vertex -0.727691 52.4235 25
      vertex -1.08156 52.3287 25
    endloop
  endfacet
  facet normal 0.258771 -0.965939 0
    outer loop
      vertex -0.727691 52.4235 25
      vertex -1.08156 52.3287 0
      vertex -0.727691 52.4235 0
    endloop
  endfacet
endsolid OpenSCAD_Model
```

### Soldering & Flex PCB

I used a flexible PCB to connect the ESP32 to the FSR and other components, which made the wiring more robust and suitable for the constant movement inside a shoe. Soldering the connections onto the flex PCB was a delicate process, but it greatly improved the durability and reliability of the system. All connections were tested for continuity and strength before final assembly.

<!-- PLACEHOLDER: Add image of soldered flex PCB and connections here -->

### Assembly & Integration

The final assembly involved attaching the battery to the ankle strap using velcro, mounting the ESP32 with the custom clip, and securing the FSR to the insole of the shoe with tape. Care was taken to ensure that all components were firmly attached but still comfortable for the user. The flex PCB allowed for easy routing of wires and minimized bulk inside the shoe. After assembly, the system was tested for fit, comfort, and functionality.

<!-- PLACEHOLDER: Add image of fully assembled SmartSole in the shoe here -->

### Challenges



### Next Steps



<!-- **Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

For your final milestone, explain the outcome of your project. Key details to include are:

- What you've accomplished since your previous milestone
- What your biggest challenges and triumphs were at BSE
- A summary of key topics you learned about
- What you hope to learn in the future after everything you've learned at BSE -->

# Second Milestone

<center><iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/NwhcUSWr9X4?si=KGRe8sVYjBnHwAYJ&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

### Description

This milestone focused on collecting sensor data and using a variety of visualizations to better understand and improve my design and code. I dedicated significant time to building a Bluetooth app for connecting to my ESP32, which proved to be much more challenging than anticipated. Attaching the device securely to my foot also required several iterations, but after some trial and error, I achieved a working prototype. With these foundations in place, I now have a functional system and am excited to keep refining it.

### Diagrams & Visualizations

To gain deeper insights into the data and system behavior, I created several types of diagrams and visualizations:

#### 1. Linear Magnitude Analysis

The linear acceleration magnitude (linmag) was the most important signal for detecting steps, jumps, and other activities. I focused on several visualizations and analyses to understand and tune my algorithms:

##### a. Rolling Statistics on Linear Magnitude

<center><img src="assets/roll_linmag.png" alt="Linear Magnitude Rolling Stats" width="350" style="border-radius: 8px;"/></center>

*I calculated the linear acceleration magnitude and overlaid rolling mean and standard deviation statistics. This made it much easier to spot steps and repetitive motions, and to set robust thresholds for event detection.*

##### b. Time Series Decomposition of Linear Magnitude

<center><img src="assets/decomposition_linmag.png" alt="Decomposition of Linear Magnitude" width="350" style="border-radius: 8px;"/></center>

*I broke down the raw linmag data into trend, seasonality, and noise components. This decomposition helped me identify patterns in walking, running, and jumping, and filter out irrelevant fluctuations.*

##### c. Power Spectral Density (PSD) and FFT of Linear Magnitude

<center><img src="assets/psd_linmag.png" alt="PSD and FFT of Linear Magnitude" width="350" style="border-radius: 8px;"/></center>

*I performed a frequency analysis (FFT and power spectral density) on the linmag signal. This revealed dominant frequencies corresponding to step rates and helped distinguish between walking, running, and jumping. It was a great help for tuning my detection algorithms and understanding the periodicity of different activities.*

---

#### 2. Orientation and 3D Motion Visualizations

While linmag was the primary focus, I also used other visualizations to understand the device's behavior:

##### a. Accelerometer Orientation

<center><img src="assets/cube_orientation.gif" alt="Accelerometer Orientation GIF" width="350" style="border-radius: 8px;"/></center>

*A dynamic visualization showing a 3D cube representing the accelerometer's orientation over time as I moved. This helped me intuitively understand how the device tracked foot motion and rotations.*

##### b. 3D Acceleration Space & Trajectory

<center><img src="assets/3d_analysis.png" alt="3D Acceleration Trajectory" width="350" style="border-radius: 8px;"/></center>

*By plotting the acceleration data in 3D space, I could visualize the trajectory of my foot during different activities. This was especially useful for distinguishing between steps, jumps, and other movements. I also mapped the orientation data (pitch, roll, yaw) in a 3D plot to observe how the foot's orientation changed during various activities, which helped in fine-tuning the movement detection algorithms.*

#### 3. Electrical Schematic

<center><img src="assets/m1schem.png" alt="Milestone 1 Schematic" width="350" style="border-radius: 8px;"/></center>

*This schematic shows the wiring and electrical connections for my project during testing. It helped ensure all components were connected correctly and provided a reference for troubleshooting hardware issues.*

### Challenges

Some of the biggest challenges I faced during this milestone included:

* Developing and debugging the Bluetooth Low Energy app to reliably communicate with the ESP32
* Creating and interpreting various diagrams and visualizations of the collected data (like those described above)
* Experimenting with different ways to attach the device securely and comfortably to my foot
* Designing meaningful test cases; just walking around randomly wasn’t enough to draw useful conclusions

### Next Steps

Moving forward, I plan to make the hardware setup more robust and user-friendly by designing custom housings for the electronic components and soldering all connections onto a flexible PCB. This will improve durability and comfort, making the device much more practical for everyday use.

<!-- **Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

For your second milestone, explain what you've worked on since your previous milestone. You can highlight:

- Technical details of what you've accomplished and how they contribute to the final goal
- What has been surprising about the project so far
- Previous challenges you faced that you overcame
- What needs to be completed before your final milestone -->

# First Milestone

<center><iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/tkfaOu9K2Xo?si=E-BL46IOyioAcZT6&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

### Description

**Hardware**

The ESP32 

**Software**

In my first milestone, I focused on the algorithms that would power my project in the future. I built a few algorithms:

1. **Movement Detection**

    This algorithm is designed to optimize power usage by determining whether the user is moving. If the user is stationary, there is no need to check for steps, since movement is a prerequisite for taking a step. The algorithm works by calculating the change in pitch and roll angles between the current and previous readings. If either the change in pitch or roll exceeds a specified threshold (measured in degrees), the system considers the user to be moving. In simpler terms, if the accelerometer detects a significant enough change in orientation, movement is registered. While developing this algorithm, I faced challenges with the AHRS (Attitude and Heading Reference System), which sometimes failed to accurately determine the accelerometer's orientation.

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

    Time Complexity: $$O\left(1\right)$$

    Space Complexity: $$O\left(1\right)$$

2. **Step Detection**

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

        if (count >= 50) {                                     //every 50 samples, update the dynamic threshold (50 is arbitrary)
            float average = sum / count;                       //we get the average magnitude
            threshold = baseThreshold + average * 0.2f;        //then we set the threshold based on baseline and average
            sum = 0.0f; count = 0;                             //finally reset sum and count for next window
        }

        unsigned long now = millis();                          //we get current time in milliseconds

        static float lastValley = 0.0f;                        //last valley value, initialized to 0, could also be -inf
        static float lastPeak = 0.0f;                          //last peak value, initialized to 0, could also be -inf
        
        static bool detectValley = 0;                          //a flag for detecting a valley

        //detect valley: previous magnitude > last magnitude < current filtered magnitude, and last magnitude is less than 
        if (previousMagnitude > lastMagnitude && lastMagnitude < filteredMagnitude && lastMagnitude < -threshold * 0.5f) {
            lastValley = lastMagnitude; detectValley = true;
        }

        //detect peak: previous magnitude < last magnitude > current filtered magnitude, and last magnitude exceeds threshold
        bool detectPeak = (previousMagnitude < lastMagnitude) && (lastMagnitude > filteredMagnitude) && (lastMagnitude > threshold);

        bool amplitudeOk = (lastMagnitude - lastValley) > (threshold * 0.5f); //check if amplitude between last peak and last valley is above threshold

        //if a valid peak is detected, amplitude is sufficient, enough time has passed since the last step, and a valley was detected
        if (detectPeak && amplitudeOk && (now - lastStepTime) > minStepInterval && detectValley) {
            lastStepTime = now;                                //we update last step time

            stepCount++;                                       //then increment step count

            detectValley = 0;                                  //then reset valley detection flag

            lastPeak = lastMagnitude;                          //we store last peak value
        }

        previousMagnitude = lastMagnitude;                     //finally update previous magnitude for next iteration
        lastMagnitude = filteredMagnitude;                     //and update last magnitude for next iteration
    }
    ```

    Time Complexity: $$O\left(1\right)$$

    Space Complexity: $$O\left(1\right)$$

3. **Distance Estimation**

    This algorithm estimates the distance traveled by the user by combining step detection from the pedometer with dynamic stride length estimation. It calculates stride length based on the peak acceleration detected during each step, then multiplies the stride length by the number of steps taken to update the total distance. This approach adapts to the user's walking or running style for more accurate distance measurement. The only challenge I faced when creating the distance estimation algorithm was deriving the formula that I used to calculate the user's stride length.

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
                                                                //the base length is 0.45 because that is the average stride length in meters
                                                                //the scale is 0.25 because of empirical testing
                                                                //9.80665 is an exact value for gravity on earth (conversion for m/s^2 to g)

        float newStrideLength = 0.45f + 0.25f * (maxLinearMagnitude / 9.80665f - 1.0f);

        if (newStrideLength < 0.3f) newStrideLength = 0.3f;     //lower bound clamp
        if (newStrideLength > 1.2f) newStrideLength = 1.2f;     //upper bound clamp

        strideLength = newStrideLength;                         //replace the previous stride length with our current stride length

                                                                //calculate how many steps were taken since the last update
        int StepsTaken = stepCount - lastStepCount;

        distance += stepsTaken * strideLength;                  //add the distance for these steps to the total distance

        lastStepCount = stepCount;                              //update the last step count

        maxLinearMagnitude = 0.0f;                              //finally reset the maximum linear magnitude for the next iteration
    }
    ```

    Time Complexity: $$O\left(1\right)$$

    Space Complexity: $$O\left(1\right)$$

4. **FSR Variance**

    This algorithm is used to determine if the user's foot, which is pushing down on the FSR (Force Sensitive Resistor), is not applying consistent force. It uses a sliding window approach to calculate variance in the force readings over time. The algorithm maintains a circular buffer of the last 10 FSR readings and computes both the average and variance of these values. When the variance exceeds a predetermined threshold, it indicates that the user's foot pressure is inconsistent, which could signal improper form or instability. The system also includes a stability check to detect sudden large changes in force readings, and if the readings become stable again, it resets the window to the current value to establish a new baseline. This variance-based approach provides a quantitative measure of foot pressure consistency during exercise.

    ```cpp
    float fsrWindow[10];                                        //the sliding window array
                                                                //the size is the number of samples in the window

    int fsrIndex = 0;                                           //a pointer to the current index of the window

    bool fsrFullWindow = 0;                                     //flag for if the window is full

    int fsrValue = analogRead(fsr);                             //read the analog output of the fsr sensor (0-4095 on esp32)

    fsrWindow[fsrIndex++] = fsrValue;                           //add that fsr analog value to the window at the index+1 to move it to empty space
    
    if (fsrIndex>=10) {                                         //if our index is now bigger than our window size, our window is full
        fsrIndex = 0; fsrFullWIndow = true;                     //we reset the index and flag our window to be full
    }

    float fsrAverage = 0, fsrVariance = 0;                      //we initialize average and variance variables to track and calculate them

    int n = fsrFullWindow ? 10 : fsrIndex;                      //n here is the number of valid samples in the window (10 if full, otherwise its fsrIndex)

    for (int i = 0; i < n; i++) fsrAverage += fsrWindow[i];     //sum all values in the window to compute the average

    fsrAverage /= n;                                            //divide by n to get the average FSR value

    for (int i = 0; i < n; i++)                                 //now, for each value in the window
        fsrVariance += (fsrWindow[i] - fsrAverage) *            //subtract the average and square the result, then sum
                       (fsrWindow[i] - fsrAverage);

    fsrVariance /= n;                                           //divide by n to get the variance (average squared deviation)

    bool fsrStable = true;                                      //flag for if our fsr reading is stable (we assume it is right now)

    for (int i = 0; i < n; i++) {                               //for each value in the window
        if (abs(fsrWindow[i] - fsrValue) > 500) {               //if the difference between the current window sample 
                                                                //and the first read value is greater than 500 (arbitrary)

            fsrStable = 0;                                      //then we do not have a stable fsr window and need to change the flag
            break;                                              //exit the loop once we have concluded its unstable
        }
    }
    if (fsrStable&&fsrFullWindow) {                             //if we are stable and our window is full
        for (int i = 0; i < 10; i++) fsrWindow[i] = fsrValue;   //we iterate through the entire window and reset to the initial value
        fsrAverage = fsrValue;                                  //then the average gets reset as the initial value as well
        fsrVariance = 0;                                        //since we are resetting variance needs to be restored to 0
    }

    const float FSR_VAR_THRESHOLD = 175175.0f;                  //completely arbitrary value for the variance threshold

    if (fsrFullWindow&&fsrVariance>FSR_VAR_THRESHOLD) playTone(750);
                                                                //if our window is full, and our variance exceeds the threshold, we buzz

    else stopTone();                                            //otherwise we stop the tone
    ```

    Time Complexity: $$O\left(1\right)$$

    Space Complexity: $$O\left(1\right)$$

### Challenges

My main challenge in this milestone was learning how to use the AHRS and accelerometer in the beginning. Learning how the sensors worked and how their libraries were written and what each function did was a lot to do in my first week, but after that I only encountered a few hiccups here and there.

### Next Steps

In my next milestone I am aiming to assemble my whole project by beginning to attach parts and build schematics/diagrams. I may also alter my algorithms later to work with multiple sensors at once rather than just the accelerometer because the implementing the pedometer would be much easier

<!-- **Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

For your first milestone, describe what your project is and how you plan to build it. You can include:

- An explanation about the different components of your project and how they will all integrate together
- Technical progress you've made so far
- Challenges you're facing and solving in your future milestones
- What your plan is to complete your project -->

# Starter Milestone

<center><iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/2HmSv4AucCM?si=lUCH4t8UGWBSdCUS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

### Description

My starter project is a retro arcade console that allows the user to play classic video games like Tetris, Snake, and Space Invaders. The screen is constructed from two 8x8 dot matrices on the top left and has a screen capable of displaying three digits in the top right. The system can be powered by the battery pack on the back of the device or by using the Micro USB port near to the number screen. The device creates sound by using a buzzer below the red power switch. There are six yellow buttons below those components which control the elements on the screen in various games.

<center><img src="assets/image.png" alt="Device Image" width="350" style="border-radius: 8px;"/></center>

### Challenges

Some challenges I encountered while working on this project were properly soldering the parts to the board as it was time consuming and was the hardest part of this project. I also discovered near the end of the project that I had attached the battery pack backwards and had to spend time fixing my mistake.

### Next Steps

I will begin working on my intensive project after this Starter Milestone.

<!-- # Schematics -->

<!-- Here's where you'll put images of your schematics. [Tinkercad](https://www.tinkercad.com/blog/official-guide-to-tinkercad-circuits) and [Fritzing](https://fritzing.org/learning/) are both great resoruces to create professional schematic diagrams, though BSE recommends Tinkercad becuase it can be done easily and for free in the browser. -->

# Bill of Materials

<!-- Here's where you'll list the parts in your project. To add more rows, just copy and paste the example rows below.
Don't forget to place the link of where to buy each component inside the quotation marks in the corresponding row after href =. Follow the guide [here]([url](https://www.markdownguide.org/extended-syntax/)) to learn how to customize this to your project needs. -->

| **Part Name** | **Purpose** | **Price** | **Qty Required** | **Link** |
|:--:|:--:|:--:|:--:|:--:|
| ESP32 | Main microcontroller for processing sensor data and handling communication | $9.99 | 1 | <a href="https://craftyhandy.com/products/esp32-microcontroller-developed?variant=41267690373210&_gsid=uMzkBAbUT2vk">Link</a> |
| MPU-6050 IMU Module (Accelerometer/Gyroscope) | Measures acceleration and gyroscopic data to detect steps, jumps, and running | $6.99 | 1 | <a href="https://www.amazon.com/HiLetgo-MPU-6050-Accelerometer-Gyroscope-Converter/dp/B01DK83ZYQ?th=1">Link</a> |
| Force Sensitive Resistor (FSR) Sensor - Long 200mm | Detects pressure changes to monitor footfalls and activity intensity | $5.99 | 2 | <a href="https://ddrpad.com/products/force-sensitive-resistor-fsr-sensor-long-200mm-size?variant=39251887161396&_gsid=BvxQWwP1pmjv">Link</a> |
| TP4056 USB-C Charging Module | To charge the battery with USB-C | $6.74 | 1 | <a href="https://garsupply.com/en-us/products/tp4056-usb-c-type-c-combo-protection-charging-1a-lithium-battery-charging-board-module?variant=49554664718659&_gsid=GJsuveiHBC3P">Link</a> |
| Vibration Motor Module (5 Pack) | Gives haptic feedback to alert the user while running | $24.50 | 1 | <a href="https://sifosolutions.com/products/vibration-motor-module-5-pack?variant=47463109132566&_gsid=iNEdwihSUzSD">Link</a> |
| SeeedStudio Grove Buzzer Module | Emits sound alerts for user notifications | $1.90 | 1 | <a href="https://www.robotshop.com/products/seeedstudio-grove-buzzer-module?variant=42359586881697&_gsid=FuTD3wVtsaCK">Link</a> |
| Fully Flexible PCB | Integrates all electronic components into a flexible form factor suitable for insoles that are constantly changing shape | $35.00 | 1 | <a href="https://skree.us/products/fully-flexible-pcbs?variant=51374897561891&_gsid=ZVbFXJ49jfnh">Link</a> |

<!-- # Other Resources/Examples (not needed?)

One of the best parts about Github is that you can view how other people set up their own work. Here are some past BSE portfolios that are awesome examples. You can view how they set up their portfolio, and you can view their index.md files to understand how they implemented different portfolio components.

- [Example 1](https://trashytuber.github.io/YimingJiaBlueStamp/)
- [Example 2](https://sviatil0.github.io/Sviatoslav_BSE/)
- [Example 3](https://arneshkumar.github.io/arneshbluestamp/)

To watch the BSE tutorial on how to create a portfolio, click here. -->

<!-- quicklink: (https://theaaravagarwal.github.io/Aarav_BlueStampPortfolio) -->