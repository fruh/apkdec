#!/usr/bin/python
from subprocess import call
import sys
import os
from optparse import OptionParser

DIR_APKDEC = sys.path[0]
DIR_TOOLS = DIR_APKDEC + os.sep + "tools"

TOOL_DEX2JAR = DIR_TOOLS + os.sep + "dex2jar-2.0" + os.sep + "d2j-dex2jar.sh"
TOOL_APKTOOL = "java -jar " + DIR_TOOLS + os.sep + "apktool_2.2.1.jar"
TOOL_PROCYON = "java -jar " + DIR_TOOLS + os.sep + "procyon-decompiler-0.5.30.jar"


def dex2jar(apk, output, d2j_options):
    output = "%s/d2j-%s.jar" % (output, os.path.basename(apk))
    args = TOOL_DEX2JAR + " -o %s " % output + d2j_options + " " + apk

    print(80 * "=" + "\nRunning: %s" % args)
    call(args.split())

    return output


def apktool(apk, output, apktool_options):
    args = TOOL_APKTOOL + " d -o %s/apktool-%s " % (output, os.path.basename(apk)) + apktool_options + " " + apk

    print(80 * "=" + "\nRunning: %s" % args)
    call(args.split())


def procyon(jar, output, proycon_options):
    args = TOOL_PROCYON + " -o %s/procyon-%s " % (output, os.path.basename(jar)) + proycon_options + " " + jar

    print(80 * "=" + "\nRunning: %s" % args)
    call(args.split())


def main():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    parser.add_option("--out", action="store", dest="out", default=os.getcwd() + os.sep + "apkdec-out",
                      help="output directory")
    parser.add_option("--apk", action="store", dest="apk", default=None,
                      help="path to the apk file")
    parser.add_option("--d2j-options", action="store", dest="d2j_options", default="", help="additional d2j options")
    parser.add_option("--apktool-options", action="store", dest="apktool_options", default="",
                      help="additional apktool options")
    parser.add_option("--proycon-options", action="store", dest="proycon_options", default="",
                      help="additional proycon options")

    (options, args) = parser.parse_args()

    if not os.path.exists(options.out):
        os.mkdir(options.out, 0775)
    else:
        print("""Output directory "%s" already exists. Continue? [Y/n]""" % options.out)
        answer = raw_input()

        if answer is not "Y":
            print("Quitting...")
            sys.exit(0)

    if options.apk is not None:
        jar = dex2jar(options.apk, options.out, options.d2j_options)
        apktool(options.apk, options.out, options.apktool_options)
        procyon(jar, options.out, options.proycon_options)

if __name__ == "__main__":
    main()
