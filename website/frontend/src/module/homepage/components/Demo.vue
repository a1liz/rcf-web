<template>
    <div>
        <Row type="flex" justify="center" align="middle" class="code-row-bg">
            <Col span="18">
                <div>
                    <h1>Header</h1>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean euismod bibendum laoreet. Proin gravida dolor sit amet lacus accumsan et viverra justo commodo. Proin sodales pulvinar tempor. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam fermentum, nulla luctus pharetra vulputate, felis tellus mollis orci, sed rhoncus sapien nunc eget.</p>
                </div>
            </Col>
            <Col span="6">
            <Button type="primary" onclick="window.location.href='https://github.com/yun-liu/rcf'">@Github</Button>
            </Col>
        </Row>
        <Card :bordered="false" class="card">
            <p slot="title">Upload a picture</p>
            <div>
                <Upload
                    action=""
                    :before-upload="handlePicture"
                    >
                    <Button type="ghost" icon="ios-cloud-upload-outline">Select the picture to upload</Button>
                </Upload>
                <div><img :src="picUpload" class="image" v-show="picShow" /></div>
                <Button type="ghost" icon="android-sync" v-show="picShow">Translate it!</Button>
            </div>
        </Card>
        <Card :bordered="false" class="card">
            <p slot="title">Upload a package</p>
            <div>
                <Upload
                    action=""
                    :before-upload="handlePackage"
                    >
                    <Button type="ghost" icon="ios-cloud-upload-outline">Select the package to upload</Button>
                </Upload>
                <div v-show="zipShow">{{ upload }}</div>
                <div v-if="packagefile !== null">Upload file: {{ packagefile.name }} <Button type="text" @click="uploadPackage" :loading="loadingStatus">{{ loadingStatus ? 'Uploading' : 'Click to upload' }}</Button></div>
            </div>
        </Card>
    </div>
</template>
<script>
export default {
    data() {
        return {
            defaultList: [

            ],
            imgName: '',
            visible: false,
            picturefile: null,
            packagefile: null,
            loadingStatus: false,
            picUpload: '',
            zipUpload: '',
            picShow: false,
            zipShow: false,
        }
    },
    methods: {
        getCookie (cName) {
        if (document.cookie.length > 0) {
          let cStart = document.cookie.indexOf(cName + '=')
          if (cStart !== -1) {
            cStart = cStart + cName.length + 1
            let cEnd = document.cookie.indexOf(';', cStart)
            if (cEnd === -1) {
              cEnd = document.cookie.length
            }
            return unescape(document.cookie.substring(cStart, cEnd))
          }
        }
        return ''
      },
        handleFormatError(file) {
            this.$Notice.warning({
                title: 'The file format is incorrect',
                desc: 'File format of ' + file.name + 'is incorrect, please select zip.'
            });
        },
        mounted() {
            this.uploadList = this.$refs.upload.fileList;
        },
        handlePicture(file) {
            this.picShow = false
            let patt = /.*\.(png|jpg|jpeg)/i
            if (!patt.test(file.name)) {
                this.$Notice.warning({
                    title: 'The file format is incorrect',
                    desc: 'file format of ' + file.name + ' is incorrect, please select jpg/jpeg/png'
                })
                return false
            }
            if (file.size > 3 * 1000 * 1000) {
                this.$Notice.warning({
                    title: 'The file size is too large',
                    desc: 'Please choose a file less than 3MB.'
                })
                return false
            }
            let pic = new FormData()
            pic.append('pic',file)
            fetch('/api/user/storepic/', {
                method: 'post',
                credentials: 'same-origin',
                headers: {
                    'X-CSRFToken': this.getCookie('csrftoken'),
                    'Accept': 'application/json'
                },
                body : pic
            }).then((res) => res.json()).then((res) => {
                this.picUpload = res['url']
            })
            setTimeout(() => {
                this.$Message.success('Success')
                this.picShow = true
            }, 1500)
            return false
        },
        handlePackage(file) {
            this.zipShow = false
            let patt = /.*\.(zip|rar)/i
            // 检测文件类型
            if (!patt.test(file.name)) {
                this.$Notice.warning({
                    title: 'The file format is incorrect',
                    desc: 'file format of  ' + file.name + '  is incorrect, please select zip/rar.'
                })
                return false
            }
            if (file.size > 20 * 1000 * 1000) {
                this.$Notice.warning({
                    title: 'The file size is too large',
                    desc: 'Please choose a file less than 20MB.'
                })
                return false
            }
            this.packagefile = file
            return false
        },
        uploadPackage() {
            let zip = new FormData()
            zip.append('zip',this.packagefile)
            fetch('/api/user/storezip/', {
                method: 'post',
                credentials: 'same-origin',
                headers: {
                    'X-CSRFToken': this.getCookie('csrftoken'),
                    'Accept': 'application/json'
                },
                body : zip
            }).then((res) => res.json()).then((res) => {
                this.zipUpload = res['url']
            })
            this.loadingStatus = true
            setTimeout(() => {
                this.packagefile = null;
                this.loadingStatus = false;
                this.$Message.success('Success')
                this.zipShow = true
            }, 1500)
            return false
        }
    }
}
</script>
<style>
 .demo-upload-list{
    display: inline-block;
    width: 60px;
    height: 60px;
    text-align: center;
    line-height: 60px;
    border: 1px solid transparent;
    border-radius: 4px;
    overflow: hidden;
    background: #fff;
    position: relative;
    box-shadow: 0 1px 1px rgba(0,0,0,.2);
    margin-right: 4px;
}
.demo-upload-list img{
    width: 100%;
    height: 100%;
}
.demo-upload-list-cover{
    display: none;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0,0,0,.6);
}
.demo-upload-list:hover .demo-upload-list-cover{
    display: block;
}
.demo-upload-list-cover i{
    color: #fff;
    font-size: 20px;
    cursor: pointer;
    margin: 0 2px;
}
.code-row-bg {
    margin-bottom: 50px;
}
.upload-card {
    margin-bottom: 100px;
}
.image {
    max-height: 100px;
}
.card {
    margin-top: 20px;
}
</style>
