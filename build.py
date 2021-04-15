#!/usr/bin/python

import os
import platform
import sys

images={
    "nginx":"registry.cn-qingdao.aliyuncs.com/kubeoperator/nginx:1.19.2-t",
    "mysql-server":"registry.cn-qingdao.aliyuncs.com/kubeoperator/mysql-server:8.0.23-t",
    "nexus":"registry.cn-qingdao.aliyuncs.com/kubeoperator/nexus:3.30.0-t",
}

class Component:
    def __init__(self,name,image):
        self.name=name
        arch=platform.machine()
        if arch in ["x86_64","AMD64"]:
            arch="amd64"
        if arch in ["ARM64","aarch64"]:
            arch="arm64"
        self.image="{}-{}".format(image,arch)

    def build(self):
        cwd=os.getcwd()
        p=os.path.join(cwd,self.name)
        print "go to dir {}".format(p)
        os.chdir(p)
        os.system("docker build -t {} .".format(self.image))
        print "return root dir"
        os.chdir(cwd)
    def push(self):
        os.system("docker push {}".format(self.image))



if __name__ == '__main__':
    
    components=[]
    for key in images.keys():
        components.append(Component(key,images[key]))
    for c in  components:
        print "build {} ...".format(c.name)
        c.build()

    if len(sys.argv)>2 and sys.argv[1]=="push":
        for c in components:
            print "push {} ...".format(c.image)
            c.push()




