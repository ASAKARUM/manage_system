<template>
  <div>
    <div v-if="isSession">
    <el-table :data="tableData" stripe v-if="currValue === '3'"
    class='demos' height="400">
      <el-table-column prop="id" label="课程序号" width="180">
      </el-table-column>
      <el-table-column prop="course" label="课程名" width="180">
      </el-table-column>
      <el-table-column prop="sec" label="总课时" width="180">
      </el-table-column>
      <el-table-column prop="name" label="孩子姓名" width="180">
      </el-table-column>
      <el-table-column prop="teacher" label="老师姓名" width="180">
      </el-table-column>
      <el-table-column label="查看课节" width="120">
        <template slot-scope="scope">
          <el-button size="small" @click="changeShow(scope.$index, scope.row)">
            查看</el-button>
        </template>
      </el-table-column>
    </el-table>
    </div>
    <div v-else>
      <el-table key="aTable" :data="sessionData" stripe v-if="currValue === '3'"
      class='demos' height="400">
        <el-table-column prop="course_id" label="课程序号" width="80">
        </el-table-column>
        <el-table-column prop="count" label="课节序号" width="80">
        </el-table-column>
        <el-table-column prop="ses_name" label="课节名称" width="150">
        </el-table-column>
        <el-table-column prop="date" label="日期" width="160">
        </el-table-column>
        <el-table-column prop="start_time" label="开始时间" width="160">
        </el-table-column>
        <el-table-column prop="end_time" label="结束时间" width="160">
        </el-table-column>
        <el-table-column prop="location" label="上课地点" width="160">
        </el-table-column>
        <el-table-column prop="is_cancel" label="是否销课" width="80">
        </el-table-column>
      </el-table>
      <div class="ass">
        <el-button @click="changeNotShow()" class="btn" round="true">
          返回</el-button>
      </div>
    </div>
  </div>
</template>

<script>
/**
 * 家长查看孩子课程信息和课节信息
 * @module syllabus
 */
import { getCookie } from '@/utils/utils';
import DIC from '@/dictionary.json';

export default {
  props: {
    initial: {
      default: '0',
    },
  },
  /**
   * @prop {String} currValue 更改页面内容
   * @prop {Boolean} isTrans 判断是否需要重新获取课程数据
   * @prop {Boolean} isSession 判断是否需要重新获取课节数据
   * @prop {Array} tableData 存放课程信息
   * @prop {Array} sessionData 存放课节信息
   */
  data() {
    return {
      currValue: '0',
      isTrans: true,
      isSession: true,
      tableData: [],
      sessionData: [],
    };
  },
  methods: {
    /**
     * @function changeShow
     * @description 改变页面状态
     */
    changeShow(index, row) {
      this.isSession = false;
      this.sessionData = [];
      this.axios({
        method: 'post',
        url: 'customer/sections',
        data: {
          course_id: row.id,
        },
        headers: { 'X-CSRFToken': getCookie('csrftoken') },
      }).then((response) => {
        for (let i = 0; i < response.data.list.length; i += 1) {
          const session = {};
          session.course_id = response.data.list[i].course_id_id;
          session.count = response.data.list[i].count;
          session.ses_name = response.data.list[i].name;
          session.date = response.data.list[i].date;
          session.start_time = response.data.list[i].start_time;
          session.end_time = response.data.list[i].end_time;
          session.location = response.data.list[i].location;
          if (response.data.list[i].is_cancel) {
            session.is_cancel = '是';
          } else {
            session.is_cancel = '否';
          }
          this.sessionData.push(session);
        }
      });
    },
    /**
     * @function changeNotShow
     * @description 判断是否处于查看课节信息
     */
    changeNotShow() {
      this.isSession = true;
    },
  },
  watch: {
    initial(nv) {
      this.currValue = nv;
      if (nv === '3') {
        this.axios({
          method: 'post',
          url: 'customer/courses',
          headers: { 'X-CSRFToken': getCookie('csrftoken') },
        }).then((response) => {
          if (response.data.msg === DIC.STATUS_CODE.Success && this.isTrans) {
            for (let i = 1; i < response.data.list.length; i += 1) {
              const lesson = {};
              lesson.id = response.data.list[i].id;
              lesson.course = response.data.list[i].name;
              lesson.sec = response.data.list[i].total_sec;
              lesson.name = response.data.list[i].child_name;
              lesson.teacher = response.data.list[i].teacher_name;
              this.tableData.push(lesson);
            }
            this.isTrans = false;
          }
        });
      }
    },
  },
};
</script>

<style scoped>
.demos {
  margin: 0 auto;
  height: 55%;
  width: 80%;
  margin-top: 3.5%;
}
.btn {
  background-color: cornflowerblue;
  color: whitesmoke;
}
.ass {
  text-align: center;
  margin-top: 1%;
}
</style>
