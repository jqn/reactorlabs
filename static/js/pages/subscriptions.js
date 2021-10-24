$(document).ready(function () {
  var leadsForm = $(".leads-form");
  var emailInput = $("#inputEmail");
  var errorAlert = $(".error-alert");
  var successAlert = $(".success-alert");
  var subscribe = (function () {
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }

    var submitLead = function () {
      const csrftoken = getCookie("csrftoken");
      $.ajax({
        headers: { "X-CSRFToken": csrftoken },
        type: "POST",
        url: "/api/leads/",
        data: {
          name: "lead",
          email: emailInput.val(),
          message: "Home lead",
        },
        // dataType: "JSON",
        success: function (data) {
          emailInput.val("");
          successAlert.removeClass("invisible");
          setTimeout(function () {
            // Closing the alert
            successAlert.addClass("invisible");
          }, 2000);
        },
        timeout: 5000,
        // handle a non-successful response
        error: function (xhr, message, err) {
          // add the error to the dom
          errorAlert.removeClass("invisible");
          setTimeout(function () {
            // Closing the alert
            errorAlert.addClass("invisible");
          }, 2000);
        },
      });
    };
    return {
      submitLead: submitLead,
    };
  })();
  leadsForm.on("submit", function (event) {
    event.preventDefault();
    subscribe.submitLead();
  });
});
