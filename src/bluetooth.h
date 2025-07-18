#pragma once
#include <Arduino.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include <functional>
#include <map>

#define SERVICE_UUID            "f5371dca-980d-4eb1-b50e-b4a7223853c7"
#define CHARACTERISTIC_UUID     "a6269c86-5982-4b90-9ce7-c2e249f71c7c"

class BluetoothSerial {
public:
    using ReceiveCallback = std::function<void(const String&)>;
    BluetoothSerial()
        : pServer(nullptr), pCharacteristic(nullptr), deviceConnected(false), receivedValue("") , echoReceived(false), receiveCallback(nullptr) {}

    void begin(const String& deviceName = "SmartSole_ESP32") {
        BLEDevice::init(deviceName.c_str());
        pServer = BLEDevice::createServer();
        pServer->setCallbacks(new ServerCallbacks(this));
        BLEService *pService = pServer->createService(SERVICE_UUID);
        pCharacteristic = pService->createCharacteristic(
            CHARACTERISTIC_UUID,
            BLECharacteristic::PROPERTY_READ   |
            BLECharacteristic::PROPERTY_WRITE  |
            BLECharacteristic::PROPERTY_NOTIFY |
            BLECharacteristic::PROPERTY_INDICATE
        );
        pCharacteristic->setCallbacks(new CharacteristicCallbacks(this));
        pCharacteristic->addDescriptor(new BLE2902());
        pService->start();
        pServer->getAdvertising()->start();
    }

    bool isConnected() {
        return deviceConnected;
    }

    void print(const String& msg) {
        if (deviceConnected && pCharacteristic) {
            pCharacteristic->setValue(msg.c_str());
            pCharacteristic->notify();
        }
    }

    void print(const char* msg) {
        if (deviceConnected && pCharacteristic) {
            pCharacteristic->setValue(msg);
            pCharacteristic->notify();
        }
    }

    void print(char c) {
        if (deviceConnected && pCharacteristic) {
            char buf[2] = {c, '\0'};
            pCharacteristic->setValue(buf);
            pCharacteristic->notify();
        }
    }

    void print(int value) {
        print(String(value));
    }

    void print(unsigned int value) {
        print(String(value));
    }

    void print(long value) {
        print(String(value));
    }

    void print(unsigned long value) {
        print(String(value));
    }

    void print(float value, int decimalPlaces = 2) {
        print(String(value, decimalPlaces));
    }

    void print(double value, int decimalPlaces = 2) {
        print(String(value, decimalPlaces));
    }

    void print(bool value) {
        print(value ? "true" : "false");
    }

    void println() {
        print('\n');
    }

    void println(const String& msg) {
        print(msg + '\n');
    }

    void println(const char* msg) {
        print(String(msg) + '\n');
    }

    void println(char c) {
        print(String(c) + '\n');
    }

    void println(int value) {
        print(String(value) + '\n');
    }

    void println(unsigned int value) {
        print(String(value) + '\n');
    }

    void println(long value) {
        print(String(value) + '\n');
    }

    void println(long long value) {
        print(String(value) + '\n');
    }

    void println(unsigned long value) {
        print(String(value) + '\n');
    }

    void println(float value, int decimalPlaces = 2) {
        print(String(value, decimalPlaces) + '\n');
    }

    void println(double value, int decimalPlaces = 2) {
        print(String(value, decimalPlaces) + '\n');
    }

    void println(bool value) {
        print((value ? "true" : "false") + String('\n'));
    }

    void sendRaw(const uint8_t* data, size_t len) {
        if (deviceConnected && pCharacteristic) {
            pCharacteristic->setValue(const_cast<uint8_t*>(data), len);
            pCharacteristic->notify();
        }
    }

    String lastReceived() {
        String tmp = receivedValue;
        receivedValue = "";
        return tmp;
    }

    void onReceive(ReceiveCallback cb) {
        receiveCallback = cb;
    }

    void setEcho(bool enable) {
        echoReceived = enable;
    }

    void addCommand(const String& command, std::function<void(String)> action) {
        commandMap[command] = action;
    }


private:
    BLEServer* pServer;
    BLECharacteristic* pCharacteristic;
    bool deviceConnected;
    String receivedValue;
    bool echoReceived;
    ReceiveCallback receiveCallback;
    std::map<String, std::function<void(const String&)>> commandMap;

    class ServerCallbacks : public BLEServerCallbacks {
        BluetoothSerial* parent;
    public:
        ServerCallbacks(BluetoothSerial* p) : parent(p) {}
        void onConnect(BLEServer*) override {
            if (parent) parent->deviceConnected = true;
        }
        void onDisconnect(BLEServer* server) override {
            if (parent) {
                parent->deviceConnected = false;
                server->getAdvertising()->start();
            }
        }
    };

    class CharacteristicCallbacks : public BLECharacteristicCallbacks {
        BluetoothSerial* parent;
    public:
        CharacteristicCallbacks(BluetoothSerial* p) : parent(p) {}
        void onWrite(BLECharacteristic* characteristic) override {
            if (!parent) return;
            std::string rxValue = characteristic->getValue();
            String strValue = String(rxValue.c_str());
            parent->receivedValue = strValue;
            if (parent->echoReceived) {
                parent->println(strValue);
            }
            if (parent->receiveCallback) {
                parent->receiveCallback(strValue);
            }
            int spidx = strValue.indexOf(' ');
            String cmdnm = strValue;
            String args = "";
            if (spidx!=-1) {
                cmdnm = strValue.substring(0, spidx);
                args = strValue.substring(spidx+1);
            }
            auto it = parent->commandMap.find(cmdnm);
            if (it!=parent->commandMap.end()) {
                it->second(args);
            } else {
                parent->println("Unknown command: "+cmdnm);
            }
        }
    };
};
