$(document).ready(function() {

	//htmlのフォームがsubmitされた時に、main.pyのreceive_content宛にテキストエリアのid="input_data"の値を送信します。
	var count = 0;
	var maxcards = 2;
	var flag = 0;
	$('form#broadcast').submit(function(event) {
		var arr = $('.card').length;
		console.log(arr);
		count++;
        $(".row").prepend('<div class="col-xs-12 col-sm-4"><div class="card" id=card_'+count+'><a class="img-card" href="https://ja.wikipedia.org/wiki/%E5%B9%B3%E6%88%90"><img src="./images/heisei.jpg" /></a><div class="card-content"><h4 class="card-title"><a href="https://ja.wikipedia.org/wiki/%E5%B9%B3%E6%88%90"> 平成の振り返り</a></h4><table  class="t12 font12"><tr><td class="table-title">ジャンル</td><td>：</td><td class="genre">'+count+'</td></tr><tr><td class="table-title">日付</td><td>：</td><td class="date">1998/03/22</td></tr></table></div><div class="card-read-more"><a href="https://ja.wikipedia.org/wiki/%E5%B9%B3%E6%88%90" class="btn btn-link btn-block">Read More</a></div></div></div>');

		var fadein_id = '#card_'+count;
		var anim = anime.timeline();
		anim.add({
			targets: fadein_id,
			translateX: -400,
			duration: 0
		});

		anim.add({
			targets: fadein_id,
			translateX: 0,
			duration: 300,
			loop: false,
			direction: 'alternate',
			easing: 'easeOutElastic(1, 0.8)'
		});

		$('.card').each(function(){
			var index =$('.card').index(this); //何番目か
			if(flag == 0){
				if(index >= maxcards){
					$(this).addClass('disnone');
					$('.more').removeClass('disnone');
				}
			}
		});
	});

	$('#more').click(function () { 
		$('.card').each(function(){
			var index =$('.card').index(this); //何番目か
			if(index >= maxcards){
				$(this).removeClass('disnone');
				$('.more').addClass('disnone');
				$('.cl').removeClass('disnone');
				flag = 1;
			}
		});
	});
	$('#close').click(function () { 
		$('.card').each(function(){
			var index =$('.card').index(this); //何番目か
			if(index >= maxcards){
				$(this).addClass('disnone');
				$('.more').removeClass('disnone');
				$('.cl').addClass('disnone');
				flag = 0;
			}
		});
	});
	var TopBtn = $('#PageTopBtn');    
    TopBtn.hide();
    // スクロール位置が100でボタンを表示
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            TopBtn.fadeIn();
        } 
        else {
            TopBtn.fadeOut();
        }
    });
    // ボタンを押下するとトップへ移動
    TopBtn.click(function() {
        $('body,html').animate({
            scrollTop: 0
        }, 300);
        return false;
    });
});