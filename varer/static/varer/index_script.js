window.addEventListener("load", (event) => {
  const csrftoken = getCookie('csrftoken');

  const dates = document.getElementsByClassName("edit-date");
  for (let i = 0; i < dates.length; i++) {
    let date = dates[i];
    let parent = date.parentElement;
    let allowButton = parent.getElementsByClassName("allow-edit-date")[0];
    let saveButton = parent.getElementsByClassName("save-edit-date")[0];
    let status = parent.getElementsByClassName("status")[0];
    date.disabled = 'disabled';
    allowButton.addEventListener("click", (event) => {
      allowButton.hidden = 'hidden';
      saveButton.hidden = ''
      date.disabled = '';
      date.focus();
    });
    saveButton.addEventListener("click", async (event) => {
      try {
        const response = await fetch("/varer/" + date.dataset.id + "/opdater/", {
          method: "POST",
          headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/x-www-form-urlencoded"
          },
          body: "date=" + date.value,
          mode: 'same-origin'
        });
        if (!response.ok) {
          status.innerHTML = response.status;
        }
        const result = await response;
        status.innerHTML = "Gemt";
        setTimeout(() => {
          status.innerHTML = "&nbsp;";
        }, 5000);
        date.disabled = 'disabled';
        date.blur();
        allowButton.hidden = '';
        saveButton.hidden = 'hidden';
      } catch (error) {
        status.innerHTML = error.message;
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
