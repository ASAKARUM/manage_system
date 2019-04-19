<template>
<div>
    <img :src="picture">
</div>
</template>
<style scoped>
.bread {
  margin: -20px -20px 10px -20px;
  height: 40px;
  border-left: 10px solid #48576a;
  background-color: white;
}
.el-breadcrumb {
  font-size: 16px;
  line-height: 3;
}
</style>
<script>
/**
 * 二维码模块
 * @module qrcode
 */
import { getCookie } from '@/utils/utils';

export default {
  props: {
    initial: {
      default: '0',
    },
  },
  data() {
    /**
     * @prop {String} currValue 当前主页面展示模块的编号
     * @prop {String} picture 图片路径
     * @prop {String} name 当前用户的名字
     */
    return {
      currValue: '0',
      name: this.$route.params.user,
      picture: '',
    };
  },
  watch: {
    initial(nv) {
      this.currValue = nv;
      if (nv === '1') {
        this.getQRcode();
      }
    },
  },
  created() {
    this.getQRcode();
  },
  methods: {
    /**
     * @function getQRcode
     * @description 获取地推人员对应的专属二维码
     */
    getQRcode() {
      this.axios({
        method: 'post',
        url: 'user/qrcode',
        data: {
          name: this.$route.params.user,
        },
        headers: { 'X-CSRFToken': getCookie('csrftoken') },
      }).then((response) => {
        this.picture = response.data.path;
      });
    },

  },
};
</script>
