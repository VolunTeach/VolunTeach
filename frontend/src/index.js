import React, { useState } from "react";
import ReactDOM from "react-dom";
import { sendSchedule, getSchedule} from "./services/ScheduleService.js";
import { TimeGridScheduler, classes } from "react-weekly-schedule";
import "react-weekly-schedule/index.css";

const rangeStrings = [
];

const defaultSchedule = rangeStrings.map(range =>
  range.map(dateString => new Date(dateString))
);


function App() {
  const [schedule, setSchedule] = useState(defaultSchedule);

  const handleClick = () => {
    sendSchedule(schedule)
      .then(response => alert(JSON.stringify(response)))
  }

  return (
    <div
      className="root"
      style={{
        width: "100vw",
        height: "50vw",
        "--cell-height": "20px",
        "--cell-width": "50px"
      }}
    >
      <TimeGridScheduler
        classes={classes}
        style={{ width: "100%", height: "100%" }}
        originDate={new Date("2019-03-04")}
        schedule={schedule}
        onChange={setSchedule}
        visualGridVerticalPrecision={30}
        verticalPrecision={30}
        cellClickPrecision={60}
      />
      <button onClick={handleClick}>
         Send Schedule
      </button>

    </div>

  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
