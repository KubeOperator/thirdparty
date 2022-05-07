### 启动容器
```shell
docker run -tid --name kubeoperator_nginx nginx:alpine sh
```
### 删除用户
```shell
deluser sync || true && deluser shutdown || true && deluser halt || true && deluser operator || true
```
### 升级
```shell
echo > /etc/apk/repositories && echo -e "https://dl-cdn.alpinelinux.org/alpine/v3.16/main\nhttps://dl-cdn.alpinelinux.org/alpine/v3.16/community" >> /etc/apk/repositories
apk update && apk upgrade
```
### 删除证书文件
```shell
find / -regex '.*\.pem\|.*\.crt\|.*\.p12\|.*\.pfx\|.*\gitignore' -type f|xargs rm -rf
```
### 删除 curl 等组件
```shell
apk del curl
rm -rf /usr/lib/libbrotlicommon* /usr/lib/libmenuw*
```
### 导出镜像
#### amd64
```shell
docker export kubeoperator_nginx -o nginx.tar
docker import nginx.tar kubeoperator/nginx:alpine-amd64
docker push kubeoperator/nginx:alpine-amd64
```
#### arm64
```shell
docker export kubeoperator_nginx -o nginx.tar
docker import nginx.tar kubeoperator/nginx:alpine-arm64
docker push kubeoperator/nginx:alpine-arm64
```
### 推送镜像（47 服务器）
```shell
docker pull kubeoperator/nginx:alpine-arm64
docker manifest create kubeoperator/nginx:alpine kubeoperator/nginx:alpine-arm64 kubeoperator/nginx:alpine-amd64
docker manifest push kubeoperator/nginx:alpine
docker manifest rm kubeoperator/nginx:alpine
```
