export async function sendSchedule(data) {
    const response = await fetch(`/api/schedule`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({schedule: data})
      })
    return await response.json();
}
