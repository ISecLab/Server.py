#!/usr/bin/python2.6 

import socket, string, sys, shutil, os

work_dir = "/tmp/"
projects_dir = "/nfs/virtualization/GNS3Files/labs/"

def getcommands():
    def loadWorkDir(args):
        projWorkDir = projects_dir  + args[0] + os.sep + "working"
        vlanWorkDir = work_dir + args[1]
        if os.path.exists(vlanWorkDir):
            shutil.rmtree(vlanWorkDir)
        if os.path.exists(projWorkDir):
            shutil.copytree(projWorkDir,vlanWorkDir)
        print "Copy from ",projWorkDir,"to ",vlanWorkDir
   
    def saveWorkDir(args):
        projWorkDir = projects_dir  + args[0] + os.sep + "working"
        vlanWorkDir = work_dir + args[1]
        print "Copy from ",vlanWorkDir,"to ",projWorkDir
        if os.path.exists(projWorkDir):
            shutil.rmtree(projWorkDir)
        if os.path.exists(vlanWorkDir):
            shutil.copytree(vlanWorkDir,projWorkDir)
        
    def die(args):
        sys.exit(args[0])
        
    def cleanWorkDir(args):
        vlanWorkDir = work_dir + args[0]
        if os.path.exists(vlanWorkDir):
            shutil.rmtree(vlanWorkDir)
            os.mkdir(vlanWorkDir)
        
    commands = locals()
    return commands


commands =  getcommands()



HOST = "172.16.0.100" # localhost
PORT = int(sys.argv[1])
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORT))
while 1:
    print "Listenning port ",PORT
    srv.listen(1)
    sock, addr = srv.accept()
    while 1:
        instr = sock.recv(1024)
        if not instr:
            break
        print "Get from %s:%s:" % addr, instr
        args = instr.split(';')
        command = args[0]
        del args[0]
        if not commands.has_key(command):
            print "Commsnd is not defined"
            sock.send("Commfnd is not defined")
        else:
            commands[command](args)
            sock.send("Ok");
          
            
            
        
            
 

