export async function sendSchedule(scheduleData, email, duration, frequency) {
    const response = await fetch(`/api/schedule`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({schedule: scheduleData, email: email, duration: duration, frequency: frequency})
      })
    return await response.json();
}

export async function getMatch() {

  const response = await fetch('/api/schedule');
  return await response.json();
}
