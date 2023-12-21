<template>
    <div class="calculator">
      <input v-model="x" type="number" placeholder="Enter number" />
      <select v-model="operation">
        <option value="add">+</option>
        <option value="subtract">-</option>
        <option value="multiply">*</option>
        <option value="divide">/</option>
      </select>
      <input v-model="y" type="number" placeholder="Enter number" />
      <button @click="doCalculation">Calculate</button>
      <p>Result: {{ result }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        x: 0,
        y: 0,
        operation: 'add',
        result: null,
      };
    },
    methods: {
      async doCalculation() {
        const response = await fetch(`/api/calc/calculate/?operation=${this.operation}&x=${this.x}&y=${this.y}`);
        const data = await response.json();
        this.result = data.result;
      },
    },
  };
  </script>

<style scoped>
/* 在这里添加 CSS 样式 */

.calculator {
  padding: 20px;
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.calculator input[type="number"] {
  padding: 10px;
  margin: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 150px;
}

.calculator select {
  padding: 10px;
  margin: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.calculator button {
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.calculator button:hover {
  background-color: #0056b3;
}

.calculator p {
  margin-top: 20px;
  font-size: 20px;
  color: #333;
}
</style>
  