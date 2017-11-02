<template>
    <div class="layout">
        <div class="header">
        <Row>
            <Col span="8">
            <Menu mode="horizontal" :theme="theme1">
            <MenuItem href="#" title="南开大学媒体计算实验室" rel="home" name="1">
                南开大学媒体计算实验室
            </MenuItem>
            </Menu>
            </Col>
            <Col span="8">
            <Menu mode="horizontal" :theme="theme1"></Menu>
            </Col>
            <Col span="8">
            <Menu class="menu" mode="horizontal" :theme="theme1" active-name="1">
                <MenuItem name="1" v-on:click="test('Introduce')">
                    Introduce
                </MenuItem>
                <MenuItem name="2" v-on:click="test('Demo')">
                    Demo
                </MenuItem>
                <MenuItem name="3" v-on:click="test('GetPic')">
                    GetPic
                </MenuItem>
                <MenuItem name="4" v-on:click="test('Login')">
                    Login
                </MenuItem>
            </Menu>
            </Col>
        </Row>
        </div>
        <div class="layout-content">
            <div class="layout-content-main" :is="page">
            </div>
        </div>
        <div class="layout-bottom">
            2017-2018 &copy; rcf-web
        </div>
    </div>
</template>
<script>
import Introduce from "./components/Introduce.vue";
import Demo from "./components/Demo";
import GetPic from "./components/GetPic";
import Login from "./components/Login";
export default {
  components: {
      Introduce,
      Demo,
      GetPic,
      Login
  },
  data() {
      return {
          page: 'Introduce'
      };
  },
  methods: {
      test: function (name) {
          this.page = name;
          alert(name);
      }
  }
}
</script>
<style scoped>
.layout {
    background-color: #fefefe;
}
.layout-content {
    margin: auto;
    margin-left: 10%;
    margin-right:10%;
    background-color: #ffffff;
}
.layout-bottom {
    position: fixed;
    width: 100%;
    bottom: 0;
    background-color: #f2f2f2;
    text-align: center;
    height: 50px;
    line-height: 50px;
}
</style>

