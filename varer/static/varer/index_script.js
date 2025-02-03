window.addEventListener("load", (event) => {
  const csrftoken = getCookie('csrftoken');

  const dates = document.getElementsByClassName("edit-date");
  for (let i = 0; i < dates.length; i++) {
    let date = dates[i];
    let parent = date.parentElement.parentElement;
    let name = parent.getElementsByClassName("vare-name")[0].innerHTML;
    let allowButton = parent.getElementsByClassName("allow-edit-date")[0];
    let saveButton = parent.getElementsByClassName("save-edit-date")[0];
    let clearButton = parent.getElementsByClassName("clear-edit-date")[0];
    let status = parent.getElementsByClassName("status")[0];
    let strongs = parent.getElementsByClassName("no-date");
    let strong = strongs.length == 1 ? strongs[0] : null;

    async function updateDate(value, onSuccess) {
      try {
        const response = await fetch("/varer/" + date.dataset.id + "/opdater/", {
          method: "POST",
          headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/x-www-form-urlencoded"
          },
          body: "date=" + value,
          mode: 'same-origin'
        });
        if (!response.ok) {
          status.innerHTML = 'Fejl: ' + response.status;
        } else {
          const result = await response;
          status.innerHTML = "Gemt";
          setTimeout(() => {
            status.innerHTML = "&nbsp;";
          }, 5000);
          allowButton.removeAttribute('hidden');
          saveButton.setAttribute('hidden', 'hidden');
          onSuccess();
        }
      } catch (error) {
        status.innerHTML = error.message;
      }
    }

    date.setAttribute('disabled', 'disabled');
    allowButton.addEventListener("click", (event) => {
      allowButton.setAttribute('hidden', 'hidden');
      saveButton.removeAttribute('hidden');
      strong?.setAttribute('hidden', 'hidden');
      date.removeAttribute('disabled');
      date.removeAttribute('hidden');
      date.focus();
    });
    saveButton.addEventListener("click", async (event) => {
      updateDate(date.value, () => {
        date.setAttribute('disabled', 'disabled');
        date.blur();
        clearButton.removeAttribute('disabled');
      });
    });
    if (date.value == '') {
      clearButton.setAttribute('disabled', 'disabled');
    }
    clearButton.addEventListener("click", (event) => {
      if (window.confirm("Er du sikker på at du vil fjerne udløbsdatoen " + date.value + " for " + name + "?")) {
        updateDate('', () => {
          date.value = ''
          clearButton.setAttribute('disabled', 'disabled');
        });
      }
    });
  }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
