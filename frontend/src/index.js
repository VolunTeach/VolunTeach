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

const DEFAULT_DURATION = 2;
const DEFAULT_FREQUENCY = 1;


function App() {
  const [schedule, setSchedule] = useState(defaultSchedule);
  var duration = DEFAULT_DURATION;
  var frequency = DEFAULT_FREQUENCY;

  const handleClick = () => {
    var durationEle = document.getElementById("duration");
    duration = durationEle.options[durationEle.selectedIndex].text.parseFloat();

    var freqEle = document.getElementById("frequency");
    frequency = freqEle.options[freqEle.selectedIndex].text.parseInt();

    // Convert hours to 30-minute sections
    duration *= 2;
    
    // In case duration/frequency is not a number
    if (!isNaN(duration) && !isNaN(frequency)) {
      duration = duration.toFixed();

      sendSchedule(schedule, duration, frequency)
      .then(response => alert(JSON.stringify(response["name"])));
    } else {
      // Can convert to "required selection" text
      console.log("Invalid duration or frequency dropdown selection!");
    }
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

      // TODO: TEST THIS!!!!!!!!!
      <label for="duration">Session Duration (hours):</label>
      <select name="duration" id="duration">
        <option value="1">1</option>
        <option value="1.5">1.5</option>
        <option value="2">2</option>
        <option value="2.5">2.5</option>
        <option value="3">3</option>
      </select>

      // TODO: TEST THIS!!!!
      <label for="frequency">Session Frequency (per week):</label>
      <select name="frequency" id="frequency">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
      </select>

      <button onClick={handleClick}>
         Send Schedule
      </button>

    </div>

  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
