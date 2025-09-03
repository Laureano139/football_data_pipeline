const teamsTableBody = document.getElementById('teams-table-body');
const countrySelector = document.getElementById('country-selector');
const messageDisplay = document.getElementById('message');

const API_PORT = 5000;

async function fetchData() {
    const selectedCountry = countrySelector.value;
    const apiUrl = `http://localhost:${API_PORT}/footballTeamsData/${selectedCountry}`;
    
    teamsTableBody.innerHTML = '';
    messageDisplay.textContent = 'Loading data...';

    try {
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
            throw new Error(`Error: HTTP status ${response.status}`);
        }

        const teams = await response.json();
        
        if (teams.length === 0) {
            messageDisplay.textContent = `No data found for ${selectedCountry}.`;
            return;
        }

        teams.forEach(team => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${team.Team_Name}</td>
                <td>${team.Country}</td>
                <td>${team.Founded}</td>
                <td>${team.Stadium}</td>
                <td>${team.Stadium_Capacity}</td>
                <td>${team.TypeOfSurface}</td>
            `;
            teamsTableBody.appendChild(row);
        });
        messageDisplay.textContent = '';

    } catch (error) {
        console.error('Unexpected error :( -> ', error);
        messageDisplay.textContent = `Error while fetching data!`;
    }
}

countrySelector.addEventListener('change', fetchData);

document.addEventListener('DOMContentLoaded', fetchData);