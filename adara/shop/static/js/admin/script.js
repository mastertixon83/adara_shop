$(document).ready(function () {
//  TODO: Добавить обработчик для выбора пола, сделать рендерин html значений списка размерных сеток
  $('#id_gender').change(function () {
    document.getElementById('id_size').innerHTML='';
  });
  $('#id_size_cheme').change(function () { // отслеживаю событие выбора размерной сетки
      // переменные
      var id_size_cheme = $('#id_size_cheme').val();
      var send_data = {
        'id_size_cheme': id_size_cheme,
      }
      $.ajax({// создаю AJAX-вызов
            type        : 'get', // определяю тип запроса, который отправляю на сервер (GET, POST)
            url         : '/test/', // url адрес на который отправляется запрос
            data        : send_data, // данные для отправки на сервер
            dataType    : 'JSON', // какой тип данных ожидаем от сервера
          success: function (data) { // если успешно, то
             if (data.length > 0) {

                var selections = document.getElementById('id_size');
                for(i=0; i<data.length; i++)

                {
                    console.log(data[i].rus_size);
                    var opt = document.createElement('option');
                    opt.value = i+1;
                    opt.innerHTML = data[i].rus_size + ' - ' + data[i].int_size;
                    selections.appendChild(opt);
//                    selections.options.add(data[i].rus_size)
                    //<option value="1" selected="">40 - xl</option>
                }
             }
             else{
                console.log(data.message);
                document.getElementById('id_size').innerHTML='';
             }

          },
          error: function (error) { // если ошибка, то
          alert('Error' + error);
          // предупредим об ошибке
          console.log(error)
          }
      });
      return false;
  });
})