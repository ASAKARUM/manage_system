<template>
  <div class="add-student">
    <div class="input-area">
      <el-input placeholder="请输入注册电话"
                v-model="search_message.tel">
      </el-input>
    </div>
    <div class="input-area">
      <el-input placeholder="请输入孩子姓名"
                v-model="search_message.child_name">
      </el-input>
    </div>
    <el-button @click="submitSearch"
               size="large">添加</el-button>
  </div>
</template>

<script>
/**
 * 添加学生表单
 * @module
 */
export default {
  props: {
    item: {
      type: Number,
      require: true,
    },
  },
  data() {
    /**
     * @prop {Object} search_message 安排学生的姓名、电话、课程信息
     */
    return {
      search_message: {
        child_name: '',
        tel: '',
        course_id: '',
      },
    };
  },
  updated() {
    this.search_message.course_id = this.item;
  },
  methods: {
    /**
     * @function submitSearch
     * @description 将学生和课程信息提交给父组件
     */
    submitSearch() {
      if (this.search_message.child_name === '' &&
          this.search_message.tel === '') {
        this.$message('请同时填入孩子姓名和电话号码');
      } else {
        this.$emit('submitSearch', this.search_message);
      }
    },
  },
};
</script>

<style scoped>
.input-area {
  width: 80%;
  max-width: 600px;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 25px;
}
</style>
