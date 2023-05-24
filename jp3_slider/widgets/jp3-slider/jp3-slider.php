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
			'title',
			[
				'label' => __('Titre : (chiffres si vide)', 'jp3-slider' ),
				'type'  => \Elementor\Controls_Manager::TEXT,
			]
		);

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
			'switch',
			[
				'label' => esc_html__( 'Icons', 'jp3-slider' ),
				'type' => \Elementor\Controls_Manager::SWITCHER,
			]
		);

		$repeater->add_control(
			'Icon1',
			[
				'label' => __('Icon 1', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'condition' => [
					'switch' => 'yes',
				],

			]
		);

		$repeater->add_control(
			'Icon1Title',
			[
				'label' => __('Titre', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
				],
			]
		);
		$repeater->add_control(
			'Icon1Text',
			[
				'label' => __('Texte', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXTAREA,
				'input_type' => 'wysiwyg',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
				],
			]
		);

		$repeater->add_control(
			'Icon2',
			[
				'label' => __('Icon 2', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'condition' => [
					'switch' => 'yes',
				],

			]
		);

		$repeater->add_control(
			'Icon2Title',
			[
				'label' => __('Titre', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
				],
			]
		);
		$repeater->add_control(
			'Icon2Text',
			[
				'label' => __('Texte', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXTAREA,
				'input_type' => 'wysiwyg',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
				],
			]
		);

		$repeater->add_control(
			'Icon3',
			[
				'label' => __('Icon 3', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'condition' => [
					'switch' => 'yes',
				],

			]
		);

		$repeater->add_control(
			'Icon3Title',
			[
				'label' => __('Titre', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
				],
			]
		);
		$repeater->add_control(
			'Icon3Text',
			[
				'label' => __('Texte', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXTAREA,
				'input_type' => 'wysiwyg',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
				],
			]
		);

		$repeater->add_control(
			'Icon4',
			[
				'label' => __('Icon 4', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'condition' => [
					'switch' => 'yes',
				],

			]
		);

		$repeater->add_control(
			'Icon4Title',
			[
				'label' => __('Titre', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
				],
			]
		);
		$repeater->add_control(
			'Icon4Text',
			[
				'label' => __('Texte', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXTAREA,
				'input_type' => 'wysiwyg',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
				],
			]
		);

		$repeater->add_control(
			'Icon5',
			[
				'label' => __('Icon 5', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'condition' => [
					'switch' => 'yes',
				],

			]
		);

		$repeater->add_control(
			'Icon5Title',
			[
				'label' => __('Titre', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXTAREA,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
				],
			]
		);
		$repeater->add_control(
			'Icon5Text',
			[
				'label' => __('Texte', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'wysiwyg',
				'dynamic' => [
					'active' => true,
				],
				'condition' => [
					'switch' => 'yes',
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
				<div id="about__id__<?= $count ?>" class="about__container__left__elements circle__<?= $count ?>">

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
						<?php if ($item['title'] != null) : ?>
						<h3 class="about__container__title" data-title-id="<?= $count ?>">
							<a href="#about__id__<?= $count ?>"><?= $item['title'] ?></a>
						</h3>

						<?php else : ?>
							
						<p>
							<a href="#about__id__<?= $count ?>">0<?= $count; ?></a>
						</p>
						
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
						<?php endif; ?>

					</li>
				
				<?php $count = $count + 1;}}?>

				</ul>
				

				<div class="about__container__right__text__paragraph">

					<!-- Check boucle 1 2 3  -->
				<?php if ($settings['list']) { ?>
				<?php $count = 1 ?>

				<?php foreach ($settings['list'] as $index => $item) { ?>
					<?php if($item['switch'] == "") : ?>

					<p class="js__<?= $count; ?>__text"><?= $item['content'] ?></p>

					<?php else : ?>
						<div class="about__container__right__pictos__container js__<?= $count; ?>__text">
						<?php if (!empty($item['Icon1']['url'])) : ?>
							<div class="about__container__right__pictos">
								<img src="<?= $item['Icon1']['url'] ?>" alt="" class="picto__image">
								<div class="picto__container__text">
									<p class="picto__title"><?= $item['Icon1Title'] ?></p>
									<p class="picto__text"><?= $item['Icon1Text'] ?></p>
								</div>
							</div>
						<?php endif ; ?>
						<?php if (!empty($item['Icon2']['url'])) : ?>
							<div class="about__container__right__pictos">
								<img src="<?= $item['Icon2']['url'] ?>" alt="" class="picto__image">
								<div class="picto__container__text">
									<p class="picto__title"><?= $item['Icon2Title'] ?></p>
									<p class="picto__text"><?= $item['Icon2Text'] ?></p>
								</div>
							</div>
						<?php endif ; ?>
						<?php if (!empty($item['Icon3']['url'])) : ?>
							<div class="about__container__right__pictos">
								<img src="<?= $item['Icon3']['url'] ?>" alt="" class="picto__image">
								<div class="picto__container__text">
									<p class="picto__title"><?= $item['Icon3Title'] ?></p>
									<p class="picto__text"><?= $item['Icon3Text'] ?></p>
								</div>
							</div>
						<?php endif ; ?>
						<?php if (!empty($item['Icon4']['url'])) : ?>
							<div class="about__container__right__pictos">
								<img src="<?= $item['Icon4']['url'] ?>" alt="" class="picto__image">
								<div class="picto__container__text">
									<p class="picto__title"><?= $item['Icon4Title'] ?></p>
									<p class="picto__text"><?= $item['Icon4Text'] ?></p>
								</div>
							</div>
						<?php endif ; ?>
						<?php if (!empty($item['Icon5']['url'])) : ?>
							<div class="about__container__right__pictos">
								<img src="<?= $item['Icon5']['url'] ?>" alt="" class="picto__image">
								<div class="picto__container__text">
									<p class="picto__title"><?= $item['Icon5Title'] ?></p>
									<p class="picto__text"><?= $item['Icon5Text'] ?></p>
								</div>
							</div>
						<?php endif ; ?>
						</div>
						

					<?php endif ; ?>


				
				<?php $count = $count + 1;}}?>

				</div>
				

				<div class="about__container__right__text__button">


					<!-- Check boucle 1 2 3  -->

				<?php if ($settings['list']) { ?>
				<?php $count = 1 ?>

				<?php foreach ($settings['list'] as $index => $item) { ?>

					<?php if($item['switch'] == "") : ?>

						<a href="<?= $item['link']['url'] ?>" class="button__anim js__<?= $count; ?>__button">
							<div class="button__anim__circle"></div>
							<div class="button__anim__text">En savoir +</div>
						</a>
						
					<?php endif ; ?>


				
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
										<div class="button__anim__text">En savoir +</div>
									</a>
								<?php else: ?>
									<a href="<?= $item['link']['url'] ?>" class="button__anim js__<?= $count ?>__button slide__button__id " data-id="<?= $count?>">
										<div class="button__anim__circle"></div>
										<div class="button__anim__text">En savoir +</div>
									</a>
								<?php endif; ?>
							
							<?php $count = $count + 1;}}?>
					</div>


					
					
				</div>
				<div class="swiper-button-next-svg">
				<svg id="after" data-name="Calque 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 104.31 104.36">
<polyline class="line" points="44.66 32.79 59.48 52.5 44.66 72.63"/>
<circle cx="52.07" cy="52.33" r="50"/>
</svg>


				</div>
				<div class="swiper-button-prev-svg">
				<svg id="previous" data-name="Calque 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 104.31 104.36">
<polyline class="line" points="59.48 71.88 44.66 52.17 59.48 32.04"/>
<circle cx="52.07" cy="52.33" r="50"/>
</svg>


				</div> 
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

    