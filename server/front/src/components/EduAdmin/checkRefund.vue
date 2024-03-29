<template>
  <div>
    <el-table :data="refunds" stripe class="table-style course-name-span">
      <el-table-column prop="fields.course.fields.name"
                       label="课程"
                       align="center">
      </el-table-column>
      <el-table-column prop="fields.customer.fields.child_name"
                       label="学生"
                       align="center">
      </el-table-column>
      <el-table-column prop="fields.refund"
                       label="价格"
                       align="center">
      </el-table-column>
      <el-table-column prop="fields.reason"
                       label="原因"
                       align="center">
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
            <el-button @click="passRefund(scope.row)"
                       type="button"
                       size="small"
                       :disabled="!scope.row.fields.is_passed">
              {{ scope.row.fields.is_passed ? '审核已通过' : '顾问审核中' }}
            </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
/**
 * 教务老师确认退款模块
 * @module checkRefund
 */
import { getCookie } from '@/utils/utils';
import DIC from '@/dictionary.json';

export default {
  data() {
    /**
     * @prop {Array} refunds 退款信息列表
     */
    return {
      refunds: [],
    };
  },
  methods: {
    /**
     * @function passRefund
     * @description 教务老师同意退款，向后端发送退款请求并处理后端响应
     */
    passRefund(key) {
      this.axios({
        method: 'post',
        url: 'api/eduadmin_ensure_refund',
        data: {
          customer_id: key.fields.customer.pk,
          course_id: key.fields.course.pk,
        },
        headers: { 'X-CSRFToken': getCookie('csrftoken') },
      }).then((response) => {
        if (response.data.msg !== DIC.STATUS_CODE.Success) {
          this.$message.error('退款失败');
        } else {
          this.updateRefund();
        }
      });
    },
    /**
     * @function organize
     * @description 怼后端返回的课程信息、顾客信息、订单信息进行处理，组织为一个数组
     */
    organize(courses, customers, refundRecords) {
      let records = refundRecords.map((item) => {
        const record = item;
        for (let i = 0; i < customers.length; i += 1) {
          if (customers[i].pk === item.fields.customer) {
            record.fields.customer = customers[i];
            return record;
          }
        }
        return record;
      });
      records = records.map((item) => {
        const record = item;
        for (let i = 0; i < courses.length; i += 1) {
          if (courses[i].pk === item.fields.course) {
            record.fields.course = courses[i];
            return record;
          }
        }
        return record;
      });
      this.refunds = records;
    },
    /**
     * @function updateRefund
     * @description 向后段发送请求并接受后端响应更新退款信息
     */
    updateRefund() {
      this.axios({
        method: 'post',
        url: 'api/eduadmin_check_refund',
        headers: { 'X-CSRFToken': getCookie('csrftoken') },
      }).then((response) => {
        if (response.data.msg !== DIC.STATUS_CODE.Success) {
          this.$message('好像有些不对劲');
          return;
        }
        let courses = JSON.parse(response.data.courses);
        let customers = JSON.parse(response.data.customers);
        const records = JSON.parse(response.data.refund_records);
        if (courses === null || courses === undefined) {
          courses = [];
        }
        if (customers === null || courses === undefined) {
          customers = [];
        }
        this.organize(courses, customers, records);
      });
    },
  },
  created() {
    this.axios({
      method: 'post',
      url: 'api/eduadmin_check_refund',
      data: {},
      headers: { 'X-CSRFToken': getCookie('csrftoken') },
    }).then((response) => {
      let courses = JSON.parse(response.data.courses);
      let customers = JSON.parse(response.data.customers);
      let records = JSON.parse(response.data.refund_records);
      if (!courses) {
        courses = [];
      }
      if (!customers) {
        customers = [];
      }
      records = records.map((item) => {
        const record = item;
        for (let i = 0; i < customers.length; i += 1) {
          if (customers[i].pk === item.fields.customer) {
            record.fields.customer = customers[i];
            return record;
          }
        }
        return record;
      });
      records = records.map((item) => {
        const record = item;
        for (let i = 0; i < courses.length; i += 1) {
          if (courses[i].pk === item.fields.course) {
            record.fields.course = courses[i];
            return record;
          }
        }
        return record;
      });
      this.refunds = records;
    });
  },
};
</script>

