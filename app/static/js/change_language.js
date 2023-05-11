
const selectElement = document.getElementById('language');
selectElement.addEventListener('change', () => {
    const selectedLanguage = selectElement.value;
    window.location.search = `lang=${selectedLanguage}`;
});