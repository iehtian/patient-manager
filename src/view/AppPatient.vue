<template>
  <div>
    <li v-if="search">搜索条件：{{ search }}</li>
    <el-table v-if="!loading && tableRows.length" :data="tableRows" :width="700" :height="400" @row-click="turn2Detail"
      @cell-mouse-enter="handleCellMouseEnter">
      <el-table-column prop="order" label="编号" width="120" />
      <el-table-column prop="name" label="姓名" width="120" />
      <el-table-column prop="birthDate" label="出生日期" width="120" />
      <el-table-column prop="gender" label="性别" width="320" />
    </el-table>
    <p v-else-if="loading">查询中...</p>
    <div v-else-if="search" class="empty-result">
      <p>未查询到患者</p>
      <el-button type="primary" @click="goToAdd = true">
        去添加
      </el-button>
    </div>
    <p v-else>请输入搜索条件</p>

    <el-dialog v-model="goToAdd" title="Tips" width="1000" :height="800" :before-close="handleClose"
      @closed="resetForm">
      <template #header>
        <span>基础信息</span>
      </template>
      <el-form label-width="100px">
        <el-row :gutter="24">
          <el-col :span="5">
            <el-form-item label="姓名">
              <el-input v-model="new_name" />
            </el-form-item>
          </el-col>

          <el-col :span="24">
            <el-form-item label="性别">
              <el-radio-group v-model="new_gender">
                <el-radio label="M">男</el-radio>
                <el-radio label="F">女</el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>

          <el-col :span="24">
            <el-form-item label="出生日期">
              <el-date-picker v-model="new_birthDate" type="date" value-format="YYYY-MM-DD" format="YYYY-MM-DD" />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <template #footer>
        <div class="dialog-footer">

          <el-button @click="goToAdd = false">Cancel</el-button>
          <el-button type="primary" @click="add">
            add
          </el-button>
        </div>
      </template>
    </el-dialog>

  </div>
</template>


<script lang="ts" setup>
  import { ref, watch } from 'vue'
  import { useRoute } from 'vue-router'
  import apiClient from '@/api/axios'
  import type { patientRow, patientsResponse } from '@/types/patient'
  import { ElMessageBox } from 'element-plus'


  const route = useRoute()
  const search = ref<string | undefined>(undefined)
  const loading = ref(false)
  type TableRow_t = { order: string; name: string; birthDate: string; gender: string }
  const tableRows = ref<Array<TableRow_t>>([])
  const goToAdd = ref(false)

  const fetchPatients = async (search?: string) => {
    if (!search) {
      tableRows.value = []
      loading.value = false
      return
    }

    loading.value = true
    try {
      const response = await apiClient.get<patientsResponse>('patients', {
        params: { search }
      })

      const patients: patientRow[] = response.data?.patients ?? []
      console.log(patients)
      tableRows.value = patients.map((item) => {
        const [order, name, birthDate, gender] = item
        return { order, name, birthDate, gender }
      })
      console.log(tableRows.value)
    } catch (error) {
      console.error(error)
      tableRows.value = []
    } finally {
      loading.value = false
    }
  }

  watch(
    () => route.query.search,
    (val) => {
      search.value = val as string | undefined
      fetchPatients(search.value)
    },
    { immediate: true }
  )
  const turn2Detail = (row: TableRow_t) => {
    console.log('点击了行', row)
  }
  const handleCellMouseEnter = (row: TableRow_t) => {
    console.log('鼠标移入行:', row)
  }
  const new_name = ref('')
  const new_gender = ref('')
  const new_birthDate = ref<string>('')

  const handleClose = (done: () => void) => {
    ElMessageBox.confirm('Are you sure to close this dialog?')
      .then(() => {
        done()
      })
      .catch(() => {
        // catch error
      })
  }
  const add = async () => {
    try {
      console.log(new_name.value, new_birthDate.value, new_gender.value)
      const res = await apiClient.post('add_patients', {
        name: new_name.value,
        gender: new_gender.value,
        birthDate: new_birthDate.value,
      })
      console.log('Patient added successfully:', res.data)
      goToAdd.value = false
    } catch (error) {
      console.error('Failed to add patient:', error)
    }
  }
  const resetForm = () => {
    new_name.value = ''
    new_gender.value = ''
    new_birthDate.value = ''
  }
</script>
