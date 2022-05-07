### 启动容器
#### amd64
```shell
docker run -tid --name kubeoperator_kobe euler2sp10x86:ITInfra1.2.0.0.20220111 bash
docker exec -ti kubeoperator_kobe bash
```
#### arm64
```shell
docker run -tid --name kubeoperator_kobe euler2sp10arm:ITInfra1.2.0.0.20220111 bash
docker exec -ti kubeoperator_kobe bash
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
### 写 yum 仓库
#### amd64
```shell
echo > /etc/yum.repos.d/Euler-Base.repo
echo -e "[EulerOS]\nname=EulerOS\nbaseurl=http://repo.huaweicloud.com/euler/2.9/os/x86_64/\nenabled=1\ngpgcheck=1\ngpgkey=http://repo.huaweicloud.com/euler/2.9/os/RPM-GPG-KEY-EulerOS" >> /etc/yum.repos.d/Euler-Base.repo
```
#### arm64
```shell
echo > /etc/yum.repos.d/Euler-Base.repo
echo -e "[EulerOS]\nname=EulerOS\nbaseurl=http://repo.huaweicloud.com/euler/2.9/os/aarch64/\nenabled=1\ngpgcheck=1\ngpgkey=http://repo.huaweicloud.com/euler/2.9/os/RPM-GPG-KEY-EulerOS" >> /etc/yum.repos.d/Euler-Base.repo
```
### 安装 ansible
```shell
curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py \
&& python3 /tmp/get-pip.py \
&& pip3 install --no-cache-dir ansible==2.10.4 netaddr \
&& curl -sSLo /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo \
&& yum install -y sshpass \
&& yum clean all \
&& rm -rf /tmp/get-pip.py /var/cache/yum/* /etc/yum.repos.d/* /usr/local/lib64/python3.7/site-packages/markupsafe/_speedups.c \
&& find / -regex '.*\.pem\|.*\.crt\|.*\.p12\|.*\.pfx\|.*\gitignore' -type f|xargs rm -rf
```
### 卸载 curl、删除 libcurl
```shell
rpm -e --nodeps curl
rpm -e --nodeps libcurl
```
### 删除安全漏洞涉及文件
```shell
rm -rf /usr/local/lib/python3.7/site-packages/ansible_collections/ansible/windows/tests/integration/targets/win_command/files/crt_setmode.c
rm -rf /usr/local/lib/python3.7/site-packages/ansible_collections/cisco/ucs/releases/cisco-ucs-1.5.0.tar.gz
rm -rf /usr/local/lib/python3.7/site-packages/ansible_collections/cisco/ucs/releases/cisco-ucs-1.2.0.tar.gz
rm -rf /usr/local/lib/python3.7/site-packages/ansible_collections/community/general/tests/integration/targets/setup_flatpak_remote/files/repo.tar.xz
rm -rf /usr/local/lib/python3.7/site-packages/ansible_collections/community/routeros/README.md
rm -rf /usr/local/lib/python3.7/site-packages/ansible_collections/dellemc/os6/roles/os6_users/README.md
rm -rf /usr/local/lib/python3.7/site-packages/ansible_collections/community/aws/tests/integration/targets/rds_instance/defaults/main.yml
rm -rf /usr/bin/lua /usr/share/doc/rsync/savetransfer.c /usr/share/lemon/lempar.c
rm -rf /usr/local/lib/python3.7/site-packages/ansible_collections/community/general/scripts/vault/__pycache__/azure_vault.cpython-37.pyc /usr/local/lib/python3.7/site-packages/ansible_collections/community/general/scripts/vault/azure_vault.py
rm -rf /usr/lib64/libsolvext.so.1
rm -rf /usr/bin/rsync
```
### 删除ansible包含的弱密码
```shell
sed -i 's/est123/kubeoperator/g' `grep est123 /usr/local/lib/python3.7 -rl`
sed -i 's/authpass/kubeoperator/g' `grep authpass /usr/local/lib/python3.7 -rl`
sed -i 's/privpass/kubeoperator/g' `grep privpass /usr/local/lib/python3.7 -rl`
sed -i 's/abc1234/kubeoperator/g' `grep abc1234 /usr/local/lib/python3.7 -rl`
sed -i 's/system_admin/kubeoperator/g' `grep system_admin /usr/local/lib/python3.7 -rl`
sed -i 's/dbadmin/kubeoperator/g' `grep dbadmin /usr/local/lib/python3.7 -rl`
sed -i 's/3pardata/kubeoperator/g' `grep 3pardata /usr/local/lib/python3.7 -rl`
sed -i 's/netrix/kubeoperator/g' `grep netrix /usr/local/lib/python3.7 -rl`
sed -i 's/Changeme/kubeoperator/g' `grep Changeme /usr/local/lib/python3.7 -rl`
```
### 导出镜像
#### amd64
```shell
docker export kubeoperator_kobe -o euleros_kobe.tar
docker import euleros_kobe.tar kubeoperator/kobe:euler2sp10-20220111-amd64
docker push kubeoperator/kobe:euler2sp10-20220111-amd64
```
#### arm64
```shell
docker export kubeoperator_kobe -o euleros_kobe.tar
docker import euleros_kobe.tar kubeoperator/kobe:euler2sp10-20220111-arm64
docker push kubeoperator/kobe:euler2sp10-20220111-arm64
```
### 推送镜像（47 服务器）
```shell
docker pull kubeoperator/kobe:euler2sp10-20220111-arm64
docker manifest create kubeoperator/kobe:euler2sp10-20220111 kubeoperator/kobe:euler2sp10-20220111-arm64 kubeoperator/kobe:euler2sp10-20220111-amd64
docker manifest push kubeoperator/kobe:euler2sp10-20220111
docker manifest rm kubeoperator/kobe:euler2sp10-20220111
```
