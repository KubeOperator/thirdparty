### 启动容器
#### amd64
```shell
docker run -tid --name kubeoperator_server euler2sp10x86:ITInfra1.2.0.0.20220111 bash
docker exec -ti kubeoperator_server bash
```
#### arm64
```shell
docker run -tid --name kubeoperator_server euler2sp10arm:ITInfra1.2.0.0.20220111 bash
docker exec -ti kubeoperator_server bash
```
### 删除用户
```shell
userdel sync || true && userdel shutdown || true && userdel halt || true && userdel operator || true
```
### 修改密码强度 /etc/pam.d/password-auth
```shell
password    requisite     pam_cracklib.so try_first_pass retry=3 minlen=14 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=-1
password    required      pam_unix.so try_first_pass
```
### 下载二进制文件
#### amd64
```shell
echo > /etc/yum.repos.d/Euler-Base.repo && \
echo -e "[EulerOS]\nname=EulerOS\nbaseurl=http://repo.huaweicloud.com/euler/2.9/os/x86_64/\nenabled=1\ngpgcheck=1\ngpgkey=http://repo.huaweicloud.com/euler/2.9/os/RPM-GPG-KEY-EulerOS" >> /etc/yum.repos.d/Euler-Base.repo && \
cd /usr/local/bin && \
yum install -y wget && \
wget --no-check-certificate https://kubeoperator.oss-cn-beijing.aliyuncs.com/xpack-license/validator_linux_amd64 && \
wget --no-check-certificate https://kubeoperator.oss-cn-beijing.aliyuncs.com/ko-encrypt/encrypt_linux_amd64 && \
yum clean all && \
rpm -e --nodeps wget && \
rm -rf /var/cache/yum/* /etc/yum.repos.d/Euler-Base.repo
```
#### arm64
```shell
echo > /etc/yum.repos.d/Euler-Base.repo && \
echo -e "[EulerOS]\nname=EulerOS\nbaseurl=http://repo.huaweicloud.com/euler/2.9/os/aarch64/\nenabled=1\ngpgcheck=1\ngpgkey=http://repo.huaweicloud.com/euler/2.9/os/RPM-GPG-KEY-EulerOS" >> /etc/yum.repos.d/Euler-Base.repo && \
cd /usr/local/bin && \
yum install -y wget && \
wget --no-check-certificate https://kubeoperator.oss-cn-beijing.aliyuncs.com/xpack-license/validator_linux_arm64 && \
wget --no-check-certificate https://kubeoperator.oss-cn-beijing.aliyuncs.com/ko-encrypt/encrypt_linux_arm64 && \
yum clean all && \
rpm -e --nodeps wget && \
rm -rf /var/cache/yum/* /etc/yum.repos.d/Euler-Base.repo
```
### 卸载 curl、删除 libcurl
```shell
rpm -e --nodeps curl
rpm -e --nodeps libcurl
```
### 删除安全漏洞涉及文件
```shell
rm -rf /usr/bin/lua /usr/share/doc/rsync/savetransfer.c /usr/share/lemon/lempar.c
rm -rf /usr/lib64/libgnutls.so.30.25.0
```
### 删除证书文件
```shell
find / -regex '.*\.pem\|.*\.crt\|.*\.p12\|.*\.pfx\|.*\gitignore' -type f|xargs rm -rf
```
### 导出镜像
#### amd64
```shell
docker export kubeoperator_server -o euleros_server.tar
docker import euleros_server.tar kubeoperator/server:euler2sp10-20220111-amd64
docker push kubeoperator/server:euler2sp10-20220111-amd64
```
#### arm64
```shell
docker export kubeoperator_server -o euleros_server.tar
docker import euleros_server.tar kubeoperator/server:euler2sp10-20220111-arm64
docker push kubeoperator/server:euler2sp10-20220111-arm64
```
### 推送镜像（47 服务器）
```shell
docker pull kubeoperator/server:euler2sp10-20220111-arm64
docker manifest create kubeoperator/server:euler2sp10-20220111 kubeoperator/server:euler2sp10-20220111-arm64 kubeoperator/server:euler2sp10-20220111-amd64
docker manifest push kubeoperator/server:euler2sp10-20220111
docker manifest rm kubeoperator/server:euler2sp10-20220111
```
