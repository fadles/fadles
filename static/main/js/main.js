$.fn.tab = function(){
	var $el = $(this),
		$tabs = $el.find('.b-product-tables__tabs li'),
		$contents = $el.find('.b-product-tables__content li');

	$contents.hide().first().show();
	$tabs.first().addClass('active');
	$tabs.on('click',function(){
		$that = $(this);
		$that.addClass('active').siblings().removeClass('active');
		var num = $that.data('tab');
		$contents.hide().filter("[data-tab='"+num+"']").show();
	});
}
$(function(){
	$('.b-product-gallery__more').on('click',function(){
		$('.b-product-gallery__main a').click();
	});
	$('.b-product__tables').tab();
});

