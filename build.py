#!/usr/bin/python

import os
import platform

images={
    "nginx":"registry.cn-qingdao.aliyuncs.com/kubeoperator/nginx:1.19.2",
    "mysql-server":"registry.cn-qingdao.aliyuncs.com/kubeoperator/mysql-server:8.0.21",
    "nexus":"registry.cn-qingdao.aliyuncs.com/kubeoperator/nexus:3.25.0",
}

class Component:
    def __init__(self,name,image):
        self.name=name
        arch=platform.machine()
        if arch in ["x86_64","AMD64"]:
            arch="amd64"
        if arch in ["ARM64"]:
            arch="arm64"
        self.image="{}-{}".format(image,arch)

    def build(self):
        cwd=os.getcwd()
        p=os.path.join(cwd,self.name)
        print "go to dir {}".format(p)
        os.chdir(p)
        os.execvpe("docker",["","build","-t",self.image,"."],os.environ)
        print "return root dir"
        os.execvpe("docker",["","push",self.image],os.environ)
        os.chdir(cwd)



if __name__ == '__main__':
    components=[]
    for key in images.keys():
        components.append(Component(key,images[key]))
    for c in  components:
        print "build {} ...".format(c.name)
        c.build()
    



