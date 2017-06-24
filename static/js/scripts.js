function request(url, handlers) {
  var r = new XMLHttpRequest();
  r.open('GET', url, true);
  r.onload = function() {
    handlers.success(this.status, JSON.parse(this.response));
  };
  r.onerror = handlers.error; // Some error communicating with server
  r.send();
}

function report(results) {
  ['result', 'error'].forEach(function(item) {
    let div = document.getElementById(item);

    if(results[item] === undefined) {
      if(!div.classList.contains('hidden')) {
        div.classList.add('hidden');
      }
    } else {
      div.innerHTML = results[item];
      if(div.classList.contains('hidden')) {
        div.classList.remove('hidden');
      }
    }
  });
}

var form = document.getElementById('form');

form.addEventListener('submit', function(e) {
  e.preventDefault();

  let link = form.elements['link'].value;

  // TODO Show the path taken to get to the link
  
  request('/api/v1/expand-link?link=' + link, {
    success: function(status, responseJSON) {
      if(status === 200) {
        report({ result: responseJSON.result });
      } else if(400 <= status && status < 500) {
        report({ error: responseJSON.message });
      } else {
        report({ error: 'The server returned a ' + status + ' response' });
      }
    },
    error: function(e) {
      report({ error: 'There was an error communicating with the server' });
    }
  });
});
