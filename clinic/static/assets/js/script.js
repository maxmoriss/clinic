$(function(){
    function getHours(){
        if (!$('[name="doctor"]').val() || !$('.datepicker').val()){
            return;
        }
        $.getJSON('/get_hours/', {
            doctor: $('[name="doctor"]').val(),
            date: $('.datepicker').val(),
            }, 
            function(json){
                $('.chose-time').show();
                $('.hours').empty();
                $.each(json, function(key, value){
                    $('.hours').append('<div class="hours__item'+(value.busy ? ' disable' : '')+'">'+value.hour+'</div>');
                });
                $('.hours__item').bind('click', function(){
                    if (!$(this).hasClass('disable')){
                        $('.hours__item').removeClass('active');
                        $(this).toggleClass('active');
                        $('[name="start_at"]').val($('.datepicker').val() + ' ' + $(this).text());
                    }
                });
        });
    }

    $('.datepicker').pickadate({
        disable: [
            6, 7
        ],
        format: 'dd.mm.yyyy',
        onSet: function(){
            getHours();
        }
    });

    $('[name="doctor"]').change(function(){
        getHours();
    });
});