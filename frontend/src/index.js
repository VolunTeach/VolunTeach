import React, { useState } from "react";
import ReactDOM from "react-dom";
import { sendSchedule } from "./services/ScheduleService.js";
import { TimeGridScheduler, classes } from "react-weekly-schedule";
import "react-weekly-schedule/index.css";
import "./style/index.css"

const rangeStrings = [
];

const defaultSchedule = rangeStrings.map(range =>
  range.map(dateString => new Date(dateString))
);

const DEFAULT_DURATION = 2;
const DEFAULT_FREQUENCY = 1;


function App() {
  const [schedule, setSchedule] = useState(defaultSchedule);

  var email = "";
  var duration = DEFAULT_DURATION;
  var frequency = DEFAULT_FREQUENCY;

  const handleClick = () => {
    var emailEle = document.getElementById("email");
    console.log(emailEle.options[emailEle.selectedIndex].text);
    email = emailEle.options[emailEle.selectedIndex].text;

    var durationEle = document.getElementById("duration");
    console.log(durationEle.options[durationEle.selectedIndex].text);
    duration = parseFloat(durationEle.options[durationEle.selectedIndex].text);

    var freqEle = document.getElementById("frequency");
    console.log(freqEle.options[freqEle.selectedIndex].text);
    frequency = parseInt(freqEle.options[freqEle.selectedIndex].text);

    // Convert hours to 30-minute sections
    duration *= 2;
    
    // Check for NaN
    if (isNaN(duration) || isNaN(frequency)) {
      // In case duration/frequency is not a number
      // Can convert to "required selection" text
      console.log("Invalid duration or frequency dropdown selection!");
      document.getElementById("event-text").textContent = "Invalid duration or frequency dropdown selection!";

    } else if (!email) {
      // In case email is empty
      // Can convert to "required email entry" text
      console.log("Email empty or invalid!");
      document.getElementById("event-text").textConent = "Empty email field!";
      
    } else {
      duration = duration.toFixed();

      // Change text on screen to show result
      sendSchedule(schedule, email, duration, frequency)
      .then(response => document.getElementById("event-text").textContent = response["name"]);
    }
  }

  // Real email should NOT be a preset name
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
        style={{ width: "100%", height: "85%" }}
        originDate={new Date("2019-03-04")}
        schedule={schedule}
        onChange={setSchedule}
        visualGridVerticalPrecision={30}
        verticalPrecision={30}
        cellClickPrecision={60}
      />

      <label for="email">Client:</label>
      <select name="email" id="email">
        <option value="Anna Apple">Anna Apple</option>
        <option value="Beth Baker">Beth Baker</option>
        <option value="Cathy Cone">Cathy Cone</option>
      </select>

      <br></br>

      <label for="duration">Session Duration (hours):</label>
      <select name="duration" id="duration">
        <option value="1">1</option>
        <option value="1.5">1.5</option>
        <option value="2">2</option>
        <option value="2.5">2.5</option>
        <option value="3">3</option>
      </select>

      <br></br>

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

      <br></br>
      
      <p id="event-text"></p>

      <button onClick={handleClick}>
         Send Schedule
      </button>

    </div>

  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
