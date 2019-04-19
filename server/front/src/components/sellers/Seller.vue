<template>
    <el-container>
      <el-header><headbar></headbar></el-header>
        <el-container>
        <el-aside width="200px">
        <el-menu
            class="el-menu-vertical-demo"
            background-color="#48576a"
            text-color="#bfcbd9"
            active-text-color="#66b1ff">
          <el-menu-item index="1" @click="onQRcode()">
          <i class="el-icon-mobile-phone"></i>
          <span slot="title">获取二维码</span>
          </el-menu-item>
          <el-menu-item index="2" @click="onSales()">
          <i class="el-icon-document"></i>
          <span slot="title">查看业绩</span>
          </el-menu-item>
          <el-menu-item index="3" @click="onPassword()">
          <i class="el-icon-setting"></i>
          <span slot="title">修改密码</span>
          </el-menu-item>
        </el-menu>
        </el-aside>
          <el-main>
          <transition name="el-zoom-in-center">
          <changepass  v-if="showindex === 3" :initial="initial"></changepass>
          <qrcode  v-if="showindex === 1" :initial="initial"></qrcode>
          <sales v-if="showindex === 2" :initial="initial"></sales>
          </transition>
      </el-main>
    </el-container>
  </el-container>
</template>
<style scoped>
.el-menu-vertical-demo {
  background-color: #909399;
}
.el-submenu__title {
  background-color: #48576a;
}
.el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
}
.el-aside {
  background-color: #48576a;
  color: #333;
  text-align: left;
  line-height: 200px;
  min-height: 960px;
}
.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
}
body > .el-container {
  margin-bottom: 40px;
}
.el-submenu__title {
  color: #715b5b;
}
.el-menu-item {
  color: #715b5b;
}
.el-menu-item is-active{
  color: #daa103;
}
.el-input__inner {
  margin-left: 0;
}
.el-menu {
  border-right: 0;
}
</style>
<script>
/**
 * 地推人员主页面
 * @module Seller
 */
import headbar from '@/components/cc/headbar';
import changepass from '@/components/cc/changepass';
import qrcode from './qrcode';
import sales from './sales';

const im = require('../../assets/headpic.png');

export default {
  components: {
    changepass,
    headbar,
    qrcode,
    sales,
  },
  data() {
    /**
     * @prop {String} name 当前用户的名字
     * @prop {String} imgUrl 图片路径
     * @prop {String} initial 当前展示模块的编号
     */
    return {
      showindex: 1,
      name: this.$route.params.user,
      imgUrl: im,
      initial: '0',
    };
  },
  methods: {
    /**
     * @function onQRcode
     * @description 控制二维码模块的展示与否
     */
    onQRcode() {
      this.showindex = 1;
      this.initial = '1';
    },
    /**
     * @function onSales
     * @description 控制销售业绩模块的展示与否
     */
    onSales() {
      this.showindex = 2;
      this.initial = '2';
    },
    /**
     * @function onPassword
     * @description 控制修改密码模块的展示与否
     */
    onPassword() {
      this.showindex = 3;
      this.initial = '3';
    },
  },
};
</script>
