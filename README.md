# apkdec
Apkdec is a simple tool/wrapper for decompiling apk.

## Description
This tool is a wrapper for external tools mentioned at the bottom. It makes them easier to use. The most simple usage takes only apk file and does the follwong:
- decompiles it to smali
- builds jar file
- decompiles jar file into java

## Usage
--------------------
```
Usage: apkdec.py [options]
Requirements
--------------------
JRE 1.7 (Java Runtime Environment)
Python 3
Options:
  -h, --help            show this help message and exit
  --out=OUT             output directory
  --apk=APK             path to the apk file
  --d2j-options=D2J_OPTIONS
                        additional d2j options
  --apktool-options=APKTOOL_OPTIONS
                        additional apktool options
  --proycon-options=PROYCON_OPTIONS
                        additional proycon options
```

### Example
```
./apkdec.py --apk ~/projects/diva-android/apk/app-debug.apk --out ~/example-appdec
```
It provides follwoing output in ~/example-appdec:
```
apktool-app-debug.apk - direcotry dontaining decompiled apk to smali
d2j-app-debug.apk.jar - generated jar file
procyon-d2j-app-debug.apk.jar - decompiled jar to java
```

### Requirements
--------------------
- JRE >=1.7 (Java Runtime Environment)
- Python >=2.7

## Tools used 
--------------------
dex2jar : https://github.com/pxb1988/dex2jar

procyon : https://bitbucket.org/mstrobel/procyon

apktool : https://ibotpeaches.github.io/Apktool/

## Inspired by 
--------------------
https://github.com/TheZ3ro/apk2java-linux
