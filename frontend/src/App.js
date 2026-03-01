import { API_BASE_URL } from './config';
import React, { useEffect, useState } from "react";
import axios from "axios";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

function App() {

  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get(`${API_BASE_URL}/metrics`)
      .then(res => setData(res.data))
      .catch(err => console.log(err));
  }, []);

  if (!data) return <h2>Loading Factory Data...</h2>;

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>

      <h1>Factory Productivity Dashboard</h1>

      <h2>Factory Metrics</h2>

      <p>Total Units Produced: {data.factory.total_units}</p>
      <p>Total Workers Active: {data.factory.total_workers}</p>

      <h2>Worker Utilization</h2>

      <BarChart
        width={600}
        height={300}
        data={data.workers}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="worker_id" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="units_produced" />
      </BarChart>

      <h2>Workstation Production</h2>

      <BarChart
        width={600}
        height={300}
        data={data.stations}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="station_id" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="units_produced" />
      </BarChart>

    </div>
  );
}

export default App;