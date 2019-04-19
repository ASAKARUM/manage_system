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
        <el-submenu index="1">
            <template slot="title">
            <i class="el-icon-tickets"></i>
            <span>审核退费申请</span>
            </template>
            <el-menu-item-group>
              <el-menu-item  index="1-1"  @click="onRecord()">退费记录</el-menu-item>
              <el-menu-item index="1-2" @click="onRefund()">未处理申请</el-menu-item>
            </el-menu-item-group>
        </el-submenu>
        <el-menu-item index="2" v-on:click="onSignUp()">
            <i class="el-icon-edit-outline"></i>
            <span slot="title">课程报名</span>
        </el-menu-item>
        <el-menu-item index="3" @click="onSales()">
            <i class="el-icon-menu"></i>
            <span slot="title">查看业绩</span>
        </el-menu-item>
         <el-menu-item index="4" @click="onList()">
            <i class="el-icon-menu"></i>
            <span slot="title">添加试听记录</span>
        </el-menu-item>
        <el-menu-item index="5" v-on:click="onPassword()">
            <i class="el-icon-setting"></i>
            <span slot="title">修改密码</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
      <el-main>
          <changepass v-show="showpassword" :name="name" :initial="initial"></changepass>
          <refundApplication v-show="application" :name="name" :initial="initial">
          </refundApplication>
          <refundHistory v-show="history" :name="name" :initial="initial"></refundHistory>
          <salesrecords v-show="showsales" :name="name" :initial="initial"></salesrecords>
          <signup v-show="showSignUp" :name="name" :initial="initial"></signup>
          <customerlist v-show="showlist" :name="name" :initial="initial"></customerlist>
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
.el-menu {
  border-right: 0;
}
</style>
<script>
import changepass from './changepass';
import headbar from './headbar';
import refundApplication from './refundApplication';
import refundHistory from './refundHistory';
import salesrecords from './salesrecords';
import signup from './signup';
import customerlist from './customerlist';

export default {
  components: {
    changepass,
    headbar,
    refundApplication,
    refundHistory,
    salesrecords,
    signup,
    customerlist,
  },
  data() {
    /**
     * @prop {String} application 展示退款申请模块
     * @prop {boolean} history 展示退款历史模块
     * @prop {boolean} showpassword 展示修改密码模块
     * @prop {boolean} showpSignUp 展示课程报名模块
     * @prop {boolean} showpassword 展示修改密码模块
     * @prop {boolean} showsales 展示销售业绩模块
     * @prop {String} newpass 存储新密码
     * @prop {String} oldpass 存储旧密码
     * @prop {String} name 存储当前登录用户的姓名
     * @prop {boolean} showlist 展示客户信息并且添加试听记录模块
     */
    return {
      application: false,
      history: false,
      showpassword: false,
      showSignUp: false,
      showsales: false,
      refund: true,
      newpass: '',
      oldpass: '',
      name: this.$route.params.user,
      activeIndex: '1',
      initial: '0',
      showlist: false,
    };
  },
  methods: {
    /**
     * @function onList
     * @description 控制客户列表模块的显示与否
     */
    onList() {
      this.showpassword = false;
      this.showsales = false;
      this.application = false;
      this.history = false;
      this.showSignUp = false;
      this.initial = '6';
      this.showlist = true;
    },
    /**
     * @function onSales
     * @description 控制业绩展示模块的显示与否
     */
    onSales() {
      this.showlist = false;
      this.showpassword = false;
      this.showsales = true;
      this.application = false;
      this.history = false;
      this.showSignUp = false;
      this.initial = '4';
    },
    /**
     * @function onSignUp
     * @description 控制填写家长信息并报名模块的显示与否
     */
    onSignUp() {
      this.showlist = false;
      this.showpassword = false;
      this.showsales = false;
      this.application = false;
      this.history = false;
      this.showSignUp = true;
      this.initial = '3';
    },
    /**
     * @function onPassword
     * @description 控制修改密码模块的显示与否
     */
    onPassword() {
      this.showlist = false;
      this.application = false;
      this.showpassword = true;
      this.showsales = false;
      this.history = false;
      this.showSignUp = false;
      this.initial = '5';
    },
    /**
     * @function onRecord
     * @description 控制退款历史模块的显示与否
     */
    onRecord() {
      this.showlist = false;
      this.application = false;
      this.showpassword = false;
      this.showsales = false;
      this.history = true;
      this.showSignUp = false;
      this.initial = '1';
    },
    /**
     * @function onRefund
     * @description 控制申请退款模块的显示与否
     */
    onRefund() {
      this.showlist = false;
      this.showpassword = false;
      this.application = true;
      this.showsales = false;
      this.history = false;
      this.showSignUp = false;
      this.initial = '2';
    },
  },
  /**
     * @function toggleSelection
     * @description 选择表格的多行进行操作
     */
  toggleSelection(rows) {
    if (rows) {
      rows.forEach((row) => {
        this.$refs.multipleTable.toggleRowSelection(row);
      });
    } else {
      this.$refs.multipleTable.clearSelection();
    }
  },
  handleSelectionChange(val) {
    this.multipleSelection = val;
  },
};
</script>
