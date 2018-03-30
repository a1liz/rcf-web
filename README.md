# rcf-web

A web demo for rcf

## Quick Start

搭建vue.js环境 (需要node.js以及npm)

Terminal(1)

```bash
cd website/frontend
npm install # 仅第一次需要
npm run build # 使用该命令后会一直保持运行。在运行期间可以修改frontend文件夹下各前端文件，会自动进行重新构建前端文件
```

Terminal(2)

```bash
cd website

# python/python3均可
# 这一步是将website/backend/models.py内的代码对应的表部署到数据库中
python manage.py migrate

# 此命令是构建后端服务器部分，但请注意这个服务器仅适合开发使用。生产环境见后
# 完成后通过 localhost:8000 打开页面
python manage.py runserver
```

同时需要开启mysql,并且建议修改`website/website/settings.py`中的Database部分,内容如下：
（按照这个配置则需要**创建一个名为rcf的数据库**，并将root密码改为qwer123）

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rcf',
        'USER': 'root',
        'PASSWORD': 'qwer123',
        'OPTIONS':{
            'autocommit':True,
        }
    }
}
```

## 整体架构部分

前端采用的是: [Vue.js](https://cn.vuejs.org/) + [iView](https://www.iviewui.com/)（UI组件），主要代码段位于 `website/frontend/src`，通过Vue.js生成的前端文件位于`website/frontend/dist`

后端采用的是: Django(Python)，有关数据库配置以及后端API的部分在`website/backend/`，这边可以通过`python manage.py migrate`自动生成数据库内容

静态文件放在`website/static`

关于Django的各种配置文件主要在`website/website`

## 关于 docker

最初使用的是根目录下的`docker-compose.yml`进行生产环境配置，但是docker运行可能会有一些异常且不利于开发，所以如果之前没有docker的经验就不建议使用。

## 关于项目生产环境的配置

为了并发性的考虑，建议使用Django-uwsgi-Nginx搭建环境，具体搭建可以自行搜索。
