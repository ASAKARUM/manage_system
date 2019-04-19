<template>
  <div>
  <div class="bread">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>添加家长试听记录</el-breadcrumb-item>
    </el-breadcrumb>
  </div>
    <el-card shadow="hover" class="mycard">
    <el-table :data="cuslist">
      <el-table-column prop="id" label="编号"></el-table-column>
      <el-table-column prop="tel" label="家长手机号"></el-table-column>
      <el-table-column prop="child_name" label="孩子姓名"></el-table-column>
      <el-table-column prop="parent_name" label="家长姓名"></el-table-column>
      <el-table-column prop="audition_count" label="试听次数"></el-table-column>
      <el-table-column prop="is_signedup" label="是否报名"></el-table-column>
      <el-table-column>
        <template slot-scope="scope">
          <el-button @click="addRecord(scope.row)" type="text">
            添加试听记录
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    </el-card>
      <el-dialog title="添加试听记录" :visible.sync="dialogFormVisible" class="conversation">
        <el-form :model="form" :rules="rules2" ref="form">
          <el-form-item label="课节名" prop="section_name">
            <el-input v-model="form.section_name"></el-input>
          </el-form-item>
          <el-form-item label="是否报名" prop="is_signedup">
            <el-select v-model="form.is_signedup">
            <el-option label="报名" value=true></el-option>
            <el-option label="不报名" value=false></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="反馈" prop="info">
            <el-input v-model="form.info"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="submit('form')">确 定</el-button>
        </div>
      </el-dialog>
  </div>
</template>

<style scoped>
.conversation {
  width: 50%;
  margin: 0 30% 0 30%;
}
.el-table th>.cell {
  width: 100%;
}
.el-table th>.cell {
  text-align: center;
}
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
.mycard {
  min-height: 800px;
}
</style>

<script>
/**
 * 课程顾问查看用户列表并添加试听记录模块
 * @module customerlist
 */
import { getCookie } from '@/utils/utils';
import DIC from '@/dictionary.json';

export default {
  props: {
    initial: {
      default: '0',
    },
    name: {
      type: String,
      require: true,
    },
  },
  data() {
    const validatesection = (rule2, value, callback) => {
      if (value === '') {
        callback(new Error('请输入课节信息'));
      } else {
        callback();
      }
    };
    const validatesign = (rule2, value, callback) => {
      if (value === '') {
        callback(new Error('请选择是否报名'));
      } else {
        callback();
      }
    };
    const validateinfo = (rule2, value, callback) => {
      if (value === '') {
        callback(new Error('请输入反馈信息'));
      } else {
        callback();
      }
    };
    return {
    /**
     * @prop {String} dialogFormVisible 对话框显示与否
     * @prop {Object} rules2 添加试听记录表单验证规则
     * @prop {Number} currid 当前用户的id
     * @prop {String} currValue 当前展示子组件编号
     * @prop {String} username 当前登录用户姓名
     * @prop {Object} cuslist 客户列表
     * @prop {Object} form 添加试听记录的表单
     */
      rules2: {
        section_name: [{ validator: validatesection, trigger: 'blur' },
          { required: true, message: '请输入课节名', trigger: 'blur' },
        ],
        is_signedup: [{ validator: validatesign, trigger: 'blur' },
          { required: true, message: '请选择是否报名', trigger: 'blur' },
        ],
        info: [{ validator: validateinfo, trigger: 'blur' },
          { required: true, message: '请填写反馈信息', trigger: 'blur' },
        ],
      },
      dialogFormVisible: false,
      currid: 0,
      currValue: '0',
      username: '',
      cuslist: [],
      form: {
        section_name: '',
        is_signedup: true,
        info: '',
      },
    };
  },
  watch: {
    name(nv) {
      this.username = nv;
    },
    initial(nv) {
      this.currValue = nv;
      if (nv === '6') {
        this.refresh();
      }
    },
  },
  methods: {
    /**
     * @function submit
     * @description 完成表单填写
     */
    submit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.dialogFormVisible = false;
          this.axios({
            method: 'post',
            url: 'data/create_audition_records',
            data: {
              id: this.currid,
              section_name: this.form.section_name,
              is_signedup: this.form.is_signedup,
              info: this.form.info,
            },
            headers: { 'X-CSRFToken': getCookie('csrftoken') },
          }).then((response) => {
            if (response.data.msg === DIC.STATUS_CODE.Success) {
              this.$message({
                message: '成功添加记录！',
                type: 'success',
              });
            }
            if (response.data.msg === DIC.STATUS_CODE['Not Found']) {
              this.$message.error('课节不存在!');
            }
            if (response.data.msg === DIC.STATUS_CODE['User Not Found']) {
              this.$message.error('用户不存在!');
            }
          });
        } else {
          return false;
        }
        return false;
      });
    },
    /**
     * @function addRecord
     * @description 添加试听记录
     */
    addRecord(row) {
      this.currid = row.id;
      this.dialogFormVisible = true;
    },
    /**
     * @function refresh
     * @description 获取客户信息
     */
    refresh() {
      this.axios({
        method: 'post',
        url: 'api/cc_view_customers',
        headers: { 'X-CSRFToken': getCookie('csrftoken') },
      }).then((response) => {
        if (response.data.msg === DIC.STATUS_CODE.Success) {
          for (let i = 0; i < response.data.list.length; i += 1) {
            this.cuslist = response.data.list;
          }
          this.$message({
            message: '数据已更新!',
            type: 'success',
          });
        } else {
          this.$message.error('身份错误!');
        }
      });
    },
  },
};
</script>
