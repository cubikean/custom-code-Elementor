<?php
namespace Elementor;

class Jp3_Slider extends Widget_Base {

	/**
	 * Get widget name.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return string Widget name.
	 */
	public function get_name() {
		return 'jp3-slider';
	}

	/**
	 * Get widget title.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return string Widget title.
	 */
	public function get_title() {
		return 'JP3 Slider';
	}

	/**
	 * Get widget icon.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return string Widget icon.
	 */
	public function get_icon() {
		return 'eicon-slider-vertical';
	}

	/**
	 * Get widget categories.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return array Widget categories.
	 */
	public function get_categories() {
		return [ 'basic' ];
	}

	/**
	 * Register widget controls.
	 * @since 1.0.0
	 * @access protected
	 */
	protected function _register_controls() {

		/**
		 *  Here you can add your controls. The controls below are only examples.
		 *  Check this: https://developers.elementor.com/elementor-controls/
		 *
		 **/


		$this->end_controls_section();
		$this->start_controls_section(
			'content_section',
			[
				'label' => __( 'JP3 Slider', 'jp3-slider' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);

		
		$repeater = new \Elementor\Repeater();

		$repeater->add_control(
			'imageContent',
			[
				'label' => __('Image du contenu', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'dynamic' => [
					'active' => true,
				],

			]
		);
		
		$repeater->add_control(
			'imageContent2',
			[
				'label' => __('Image du contenu', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'dynamic' => [
					'active' => true,
				],

			]
		);

		$repeater->add_control(
			'content',
			[
				'label' => __('Contenu', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXTAREA,
				'input_type' => 'wysiwyg',
				'dynamic' => [
					'active' => true,
				],
			]
		);

		$repeater->add_control(
			'link',
			[
				'label' => esc_html__( 'Link', 'jp3-slider' ),
				'type' => \Elementor\Controls_Manager::URL,
				'placeholder' => esc_html__( 'https://your-link.com', 'jp3-slider' ),
				'options' => [ 'url', 'is_external', 'nofollow' ],
				'default' => [
					'url' => '',
					'is_external' => true,
					'nofollow' => true,
					// 'custom_attributes' => '',
				],
				'label_block' => true,
			]
		);

		$this->add_control(
			'list',
			[
				'label' => esc_html__('JP3 SLIDER', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::REPEATER,
				'fields' => $repeater->get_controls(),
			]
		);

		$this->end_controls_section();


	}

	/**
	 * Render widget output on the frontend.
	 *
	 * Written in PHP and used to generate the final HTML.
	 *
	 * @since 1.0.0
	 * @access protected
	 */
	protected function render() {

		$settings = $this->get_settings_for_display();

		/**
		 *  Here you can output your control data and build your content.
		 **/

 ?>
 <section class="about">

	<div class="about__container">

		<div class="about__container__left">

			
			<?php if ($settings['list']) { ?>
				<?php $count = 1 ?>

				<?php foreach ($settings['list'] as $index => $item) { ?>
			

				<!-- 1 -->
				<div class="about__container__left__elements circle__<?= $count ?>">

					<div class="first_patchwork">
						<img src="<?= $item['imageContent']['url'] ?>" />
					</div>

					<div class="second_patchwork">
						<img src="<?= $item['imageContent2']['url'] ?>" />
					</div>

				</div>

			<?php $count = $count + 1;}}?>

			<div class="elements__end">
			</div>


		</div>

		<div class="about__container__right">

			<div class="about__container__right__text">


				<ul class="about__container__right__text__counter">

				<!-- Check boucle 1 2 3  -->
				<?php if ($settings['list']) { ?>
				<?php $count = 1 ?>

				<?php foreach ($settings['list'] as $index => $item) { ?>
			
					<li>
						<p>0<?= $count; ?></p>
					
						<svg
							xmlns:dc="http://purl.org/dc/elements/1.1/"
							xmlns:cc="http://creativecommons.org/ns#"
							xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
							xmlns:svg="http://www.w3.org/2000/svg"
							xmlns="http://www.w3.org/2000/svg"
							id="circle<?= $count; ?>"
							data-name="Calque <?= $count; ?>"
							viewBox="0 0 24.68 24.81"
							version="1.1">
							<path d="M 24.3,12.36 A 11.97,11.97 0 0 1 12.33,24.33 11.97,11.97 0 0 1 0.35999966,12.36 11.97,11.97 0 0 1 12.33,0.38999939 11.97,11.97 0 0 1 24.3,12.36 Z" />
						</svg>
					</li>
				
				<?php $count = $count + 1;}}?>

				</ul>
				

				<div class="about__container__right__text__paragraph">

					<!-- Check boucle 1 2 3  -->
				<?php if ($settings['list']) { ?>
				<?php $count = 1 ?>

				<?php foreach ($settings['list'] as $index => $item) { ?>
			
					<p class="js__<?= $count; ?>__text"><?= $item['content'] ?></p>

				
				<?php $count = $count + 1;}}?>

				</div>
				

				<div class="about__container__right__text__button">


					<!-- Check boucle 1 2 3  -->

				<?php if ($settings['list']) { ?>
				<?php $count = 1 ?>

				<?php foreach ($settings['list'] as $index => $item) { ?>
			
					<a href="<?= $item['link']['url'] ?>" class="button__anim js__<?= $count; ?>__button">
						<div class="button__anim__circle"></div>
						<div class="button__anim__text">en savoir plus</div>
					</a>

				
				<?php $count = $count + 1;}}?>
						
				</div>

			</div>
		</div>
	</div>

	<div class="about__slider">

			
				<div class="swiper-container swiper-container_about">
					<div class="swiper-wrapper swiper-wrapper_about">

						<?php if ($settings['list']) { ?>
							<?php $count = 1 ?>

							<?php foreach ($settings['list'] as $index => $item) { ?>
						
								<div class="swiper-slide swiper-slide_about" data-id="<?= $count ?>">  
									<div class="swiper-slide_about__container">
										<div class="swiper-slide_about__container__first__image">
											<img src="<?= $item['imageContent']['url'] ?>" />
										</div>
										<div class="swiper-slide_about__container__second__image reverse">
											<img src="<?= $item['imageContent2']['url'] ?>" />
										</div>
									</div>
								</div>

						<?php $count = $count + 1;}}?>

					</div>
												
				</div>

				<div class="about__slider__text">

					<div class="about__slider__text__paragraph">

						<?php if ($settings['list']) { ?>
						<?php $count = 1 ?>

						<?php foreach ($settings['list'] as $index => $item) { ?>
					

							<?php if ($count == 1): ?>
									<p class="js__<?= $count ?>__text slide__text__id text__active"  data-id="<?= $count?>"><?= $item['content'] ?></p>
							<?php else: ?>
							<p class="js__<?= $count ?>__text slide__text__id"  data-id="<?= $count?>"><?= $item['content'] ?></p>

							<?php endif; ?>
						
						<?php $count = $count + 1;}}?>

					</div>

					<div class="about__slider__text__button">


						<?php if ($settings['list']) { ?>
							<?php $count = 1 ?>

							<?php foreach ($settings['list'] as $index => $item) { ?>
						
								<?php if ($count == 1): ?>
									<a href="<?= $item['link']['url'] ?>" class="button__anim js__<?= $count ?>__button slide__button__id text__active " data-id="<?= $count?>">
										<div class="button__anim__circle"></div>
										<div class="button__anim__text">en savoir plus</div>
									</a>
								<?php else: ?>
									<a href="<?= $item['link']['url'] ?>" class="button__anim js__<?= $count ?>__button slide__button__id " data-id="<?= $count?>">
										<div class="button__anim__circle"></div>
										<div class="button__anim__text">en savoir plus</div>
									</a>
								<?php endif; ?>
							
							<?php $count = $count + 1;}}?>
					</div>


					
					
				</div>
				<div class="swiper-button-next-svg"> next </div>
				<div class="swiper-button-prev-svg"> prev </div> 
		</div>
	

</section>

 <?php

	}

	/**
	 * Written as a Backbone JavaScript template and used to generate the live preview.
	 * With JS templates we don’t really need to retrieve the data using a special function, its done by Elementor for us.
	 * The data from the controls stored in the settings variable.
	 */
	protected function _content_template() {
		?>
		<section>
			La preview n'est pas disponible 
		</section>
		<?php
	}
}

    