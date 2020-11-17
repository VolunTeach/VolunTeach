export async function sendSchedule(data) {
    const response = await fetch(`/api/schedule`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({schedule: data})
      })
    return await response.json();
}

export async function getMatch() {

  const response = await fetch('/api/schedule');
  return await response.json();
}