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
				'label' => __('Contenu', 'jp3-slider'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'placeholder' => esc_html__( 'Votre contenu', 'jp3-slider' ),
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
				'default' => [
					[
						'TitleTab' => esc_html__('Titre de l\'onglet ...', 'jp3-slider'),
						'TitleContent' => esc_html__('Titre de votre contenu...', 'jp3-slider'),
						'Content' => esc_html__('Votre contenu...', 'jp3-slider'),
					],
					[
						'TitleTab' => esc_html__('Titre de l\'onglet ...', 'jp3-slider'),
						'TitleContent' => esc_html__('Titre de votre contenu...', 'jp3-slider'),
						'Content' => esc_html__('Votre contenu...', 'jp3-slider'),
					],
				],
				'title_field' => '{{{ TitleTab }}}',
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

				<div class="about__container__left__infos">
						<h2 class="home__title" data-scroll data-scroll-speed="0.75">title</h2>
				</div>

				<!-- <?php 

					$compt = 0;

					if( have_rows('patchwork') ):

						while( have_rows('patchwork') ) : the_row();

						$compt++;
							$patchwork_image_1 = get_sub_field('patchwork_image_1'); 
							$patchwork_image_2 = get_sub_field('patchwork_image_2'); ?>	


						<?php if ($compt == 1): ?> -->
		

						<div class="about__container__left__elements circle__1">

						<div class="first_patchwork">
									<img src="https://dummyimage.com/600x400/000/fff" />
							</div>

							<div class="second_patchwork">
									<img src="https://dummyimage.com/600x400/000/fff" />
							</div>

						</div>

						<!-- <?php elseif ($compt == 2): ?> -->

						<div class="about__container__left__elements circle__2">

						<div class="first_patchwork reverse">
									<img src="https://dummyimage.com/500x400/000/fff" />
							</div>

							<div class="second_patchwork reverse">
									<img src="https://dummyimage.com/500x400/000/fff" />
							</div>

						</div>

						<!-- <?php elseif ($compt == 3): ?> -->

						<div class="about__container__left__elements last circle__3">

						<div class="first_patchwork">
									<img src="https://dummyimage.com/400x400/000/fff" />
							</div>

							<div class="second_patchwork">
									<img src="https://dummyimage.com/400x400/000/fff" />
							</div>

						</div>

						<!-- <?php endif; ?>


						<?php	endwhile;
					else :
				endif; ?> -->

				<div class="elements__end">
				</div>


			</div>

			<div class="about__container__right">

				<div class="about__container__right__text">


					<ul class="about__container__right__text__counter">

					<!-- <?php 

					$compt = 0;

					if( have_rows('patchwork') ):

						while( have_rows('patchwork') ) : the_row();

						$compt++;?> -->

						<li><p>01</p>
                        
                            <svg
                            xmlns:dc="http://purl.org/dc/elements/1.1/"
                            xmlns:cc="http://creativecommons.org/ns#"
                            xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                            xmlns:svg="http://www.w3.org/2000/svg"
                            xmlns="http://www.w3.org/2000/svg"
                            id="circle1"
                            data-name="Calque 1"
                            viewBox="0 0 24.68 24.81"
                            version="1.1">
                           <path
                              d="M 24.3,12.36 A 11.97,11.97 0 0 1 12.33,24.33 11.97,11.97 0 0 1 0.35999966,12.36 11.97,11.97 0 0 1 12.33,0.38999939 11.97,11.97 0 0 1 24.3,12.36 Z" />
                         </svg>
                         </li>

                         <li><p>02</p>
                        
                            <svg
                            xmlns:dc="http://purl.org/dc/elements/1.1/"
                            xmlns:cc="http://creativecommons.org/ns#"
                            xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                            xmlns:svg="http://www.w3.org/2000/svg"
                            xmlns="http://www.w3.org/2000/svg"
                            id="circle2"
                            data-name="Calque 2"
                            viewBox="0 0 24.68 24.81"
                            version="1.1">
                           <path
                              d="M 24.3,12.36 A 11.97,11.97 0 0 1 12.33,24.33 11.97,11.97 0 0 1 0.35999966,12.36 11.97,11.97 0 0 1 12.33,0.38999939 11.97,11.97 0 0 1 24.3,12.36 Z" />
                         </svg>
                         </li>

                         <li><p>03</p>
                        
                            <svg
                            xmlns:dc="http://purl.org/dc/elements/1.1/"
                            xmlns:cc="http://creativecommons.org/ns#"
                            xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                            xmlns:svg="http://www.w3.org/2000/svg"
                            xmlns="http://www.w3.org/2000/svg"
                            id="circle3"
                            data-name="Calque 3"
                            viewBox="0 0 24.68 24.81"
                            version="1.1">
                           <path
                              d="M 24.3,12.36 A 11.97,11.97 0 0 1 12.33,24.33 11.97,11.97 0 0 1 0.35999966,12.36 11.97,11.97 0 0 1 12.33,0.38999939 11.97,11.97 0 0 1 24.3,12.36 Z" />
                         </svg>
                         </li>

						<!-- <?php	endwhile;
						else :
					endif; ?> -->
					
					</ul>
					

					<div class="about__container__right__text__paragraph">

					<!-- <?php 

					$compt = 0;

					if( have_rows('patchwork') ):

						while( have_rows('patchwork') ) : the_row();

						$compt++;
							$patchwork_text = get_sub_field('patchwork_text'); ?> -->


						<p class="js__1__text">text</p>
						<p class="js__2__text">bla</p>
						<p class="js__3__text">BLABLALBALB</p>

						<!-- <?php	endwhile;
						else :
					endif; ?> -->
					</div>
					

					<div class="about__container__right__text__button">

						<!-- <?php 

						$compt = 0;

						if( have_rows('patchwork') ):

							while( have_rows('patchwork') ) : the_row();

							$compt++;
								$patchwork_link = get_sub_field('patchwork_button_link');
								$patchwork_text = get_sub_field('patchwork_button_text'); ?>
 -->

							<a href="#link" class="button__anim js__1__button">
								<div class="button__anim__circle"></div>
								<div class="button__anim__text">text</div>
							</a>
                            <a href="#link" class="button__anim js__2__button">
								<div class="button__anim__circle"></div>
								<div class="button__anim__text">text</div>
							</a>
                            <a href="#link" class="button__anim js__3__button">
								<div class="button__anim__circle"></div>
								<div class="button__anim__text">text</div>
							</a>

						<!-- <?php
							endwhile;
							else :
						endif; ?> -->
					</div>
		
				</div>
			</div>
		</div>

		<div class="about__slider" style="display:none">

			<div class="about__slider__infos">
						<h2 class="home__title" data-scroll data-scroll-speed="0.75">title</h2>
				</div>

				<div class="swiper-container swiper-container_about">
					<div class="swiper-wrapper swiper-wrapper_about">


						<div class="swiper-slide swiper-slide_about" data-id="<?= $compt ?>">  

							<div class="swiper-slide_about__container">

								<div class="swiper-slide_about__container__first__image">

									<img src="https://dummyimage.com/600x400/000/fff" />

								</div>

								<div class="swiper-slide_about__container__second__image reverse">
									<img src="https://dummyimage.com/600x400/000/fff" />
								</div>



							</div>

						</div>

						<div class="swiper-slide swiper-slide_about" data-id="<?= $compt ?>">  
							
							<div class="swiper-slide_about__container">

								<div class="swiper-slide_about__container__first__image">

									<img src="https://dummyimage.com/600x400/000/fff" />

								</div>

								<div class="swiper-slide_about__container__second__image">
									<img src="https://dummyimage.com/600x400/000/fff" />
								</div>



							</div>

						</div>
							
					</div>

					
					 
												
				</div>

				<div class="about__slider__text">

					<div class="about__slider__text__paragraph">

						<?php 

						$compt = 0;

						if( have_rows('patchwork') ):

							while( have_rows('patchwork') ) : the_row();

							$compt++;
								$patchwork_text = get_sub_field('patchwork_text'); ?>

							<?php if ($compt == 1): ?>
								<p class="js__<?= $compt ?>__text slide__text__id text__active"  data-id="<?= $compt?>"><?= $patchwork_text ?></p>
							<?php else: ?>
							<p class="js__<?= $compt ?>__text slide__text__id"  data-id="<?= $compt?>"><?= $patchwork_text ?></p>

							<?php endif; ?>

							<?php	endwhile;
							else :
						endif; ?>
					</div>

					<div class="about__slider__text__button">

						<?php 

						$compt = 0;

						if( have_rows('patchwork') ):

							while( have_rows('patchwork') ) : the_row();

							$compt++;
								$patchwork_link = get_sub_field('patchwork_button_link');
								$patchwork_text = get_sub_field('patchwork_button_text'); ?>

							<?php if ($compt == 1): ?>
								<a href="<?= $patchwork_link ?>" class="button__anim js__<?= $compt ?>__button slide__button__id text__active " data-id="<?= $compt?>">
									<div class="button__anim__circle"></div>
									<div class="button__anim__text"><?= $patchwork_text ?></div>
								</a>
							<?php else: ?>
								<a href="<?= $patchwork_link ?>" class="button__anim js__<?= $compt ?>__button slide__button__id " data-id="<?= $compt?>">
									<div class="button__anim__circle"></div>
									<div class="button__anim__text"><?= $patchwork_text ?></div>
								</a>
							<?php endif; ?>

						<?php
							endwhile;
							else :
						endif; ?>
					</div>


					
					
				</div>
				<div class="swiper-button-next-svg"><?php include("inc/arrow-after.php")?></div>
					<div class="swiper-button-prev-svg"><?php include("inc/arrow-before.php")?></div> 
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
<section class="about">

		<div class="about__container">

			<div class="about__container__left">

				<div class="about__container__left__infos">
						<h2 class="home__title" data-scroll data-scroll-speed="0.75">title</h2>
				</div>

				<!-- <?php 

					$compt = 0;

					if( have_rows('patchwork') ):

						while( have_rows('patchwork') ) : the_row();

						$compt++;
							$patchwork_image_1 = get_sub_field('patchwork_image_1'); 
							$patchwork_image_2 = get_sub_field('patchwork_image_2'); ?>	


						<?php if ($compt == 1): ?> -->
		

						<div class="about__container__left__elements circle__1">

						<div class="first_patchwork">
									<img src="https://dummyimage.com/600x400/000/fff" />
							</div>

							<div class="second_patchwork">
									<img src="https://dummyimage.com/600x400/000/fff" />
							</div>

						</div>

						<!-- <?php elseif ($compt == 2): ?> -->

						<div class="about__container__left__elements circle__2">

						<div class="first_patchwork reverse">
									<img src="https://dummyimage.com/500x400/000/fff" />
							</div>

							<div class="second_patchwork reverse">
									<img src="https://dummyimage.com/500x400/000/fff" />
							</div>

						</div>

						<!-- <?php elseif ($compt == 3): ?> -->

						<div class="about__container__left__elements last circle__3">

						<div class="first_patchwork">
									<img src="https://dummyimage.com/400x400/000/fff" />
							</div>

							<div class="second_patchwork">
									<img src="https://dummyimage.com/400x400/000/fff" />
							</div>

						</div>

						<!-- <?php endif; ?>


						<?php	endwhile;
					else :
				endif; ?> -->

				<div class="elements__end">
				</div>


			</div>

			<div class="about__container__right">

				<div class="about__container__right__text">


					<ul class="about__container__right__text__counter">

					<!-- <?php 

					$compt = 0;

					if( have_rows('patchwork') ):

						while( have_rows('patchwork') ) : the_row();

						$compt++;?> -->

						<li><p>01</p>
                        
                            <svg
                            xmlns:dc="http://purl.org/dc/elements/1.1/"
                            xmlns:cc="http://creativecommons.org/ns#"
                            xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                            xmlns:svg="http://www.w3.org/2000/svg"
                            xmlns="http://www.w3.org/2000/svg"
                            id="circle1"
                            data-name="Calque 1"
                            viewBox="0 0 24.68 24.81"
                            version="1.1">
                           <path
                              d="M 24.3,12.36 A 11.97,11.97 0 0 1 12.33,24.33 11.97,11.97 0 0 1 0.35999966,12.36 11.97,11.97 0 0 1 12.33,0.38999939 11.97,11.97 0 0 1 24.3,12.36 Z" />
                         </svg>
                         </li>

                         <li><p>02</p>
                        
                            <svg
                            xmlns:dc="http://purl.org/dc/elements/1.1/"
                            xmlns:cc="http://creativecommons.org/ns#"
                            xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                            xmlns:svg="http://www.w3.org/2000/svg"
                            xmlns="http://www.w3.org/2000/svg"
                            id="circle2"
                            data-name="Calque 2"
                            viewBox="0 0 24.68 24.81"
                            version="1.1">
                           <path
                              d="M 24.3,12.36 A 11.97,11.97 0 0 1 12.33,24.33 11.97,11.97 0 0 1 0.35999966,12.36 11.97,11.97 0 0 1 12.33,0.38999939 11.97,11.97 0 0 1 24.3,12.36 Z" />
                         </svg>
                         </li>

                         <li><p>03</p>
                        
                            <svg
                            xmlns:dc="http://purl.org/dc/elements/1.1/"
                            xmlns:cc="http://creativecommons.org/ns#"
                            xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                            xmlns:svg="http://www.w3.org/2000/svg"
                            xmlns="http://www.w3.org/2000/svg"
                            id="circle3"
                            data-name="Calque 3"
                            viewBox="0 0 24.68 24.81"
                            version="1.1">
                           <path
                              d="M 24.3,12.36 A 11.97,11.97 0 0 1 12.33,24.33 11.97,11.97 0 0 1 0.35999966,12.36 11.97,11.97 0 0 1 12.33,0.38999939 11.97,11.97 0 0 1 24.3,12.36 Z" />
                         </svg>
                         </li>

						<!-- <?php	endwhile;
						else :
					endif; ?> -->
					
					</ul>
					

					<div class="about__container__right__text__paragraph">

					<!-- <?php 

					$compt = 0;

					if( have_rows('patchwork') ):

						while( have_rows('patchwork') ) : the_row();

						$compt++;
							$patchwork_text = get_sub_field('patchwork_text'); ?> -->


						<p class="js__1__text">text</p>
						<p class="js__2__text">bla</p>
						<p class="js__3__text">BLABLALBALB</p>

						<!-- <?php	endwhile;
						else :
					endif; ?> -->
					</div>
					

					<div class="about__container__right__text__button">

						<!-- <?php 

						$compt = 0;

						if( have_rows('patchwork') ):

							while( have_rows('patchwork') ) : the_row();

							$compt++;
								$patchwork_link = get_sub_field('patchwork_button_link');
								$patchwork_text = get_sub_field('patchwork_button_text'); ?>
 -->

							<a href="#link" class="button__anim js__1__button">
								<div class="button__anim__circle"></div>
								<div class="button__anim__text">text</div>
							</a>
                            <a href="#link" class="button__anim js__2__button">
								<div class="button__anim__circle"></div>
								<div class="button__anim__text">text</div>
							</a>
                            <a href="#link" class="button__anim js__3__button">
								<div class="button__anim__circle"></div>
								<div class="button__anim__text">text</div>
							</a>

						<!-- <?php
							endwhile;
							else :
						endif; ?> -->
					</div>
		
				</div>
			</div>
		</div>

		<div class="about__slider" style="display:none">

			<div class="about__slider__infos">
						<h2 class="home__title" data-scroll data-scroll-speed="0.75">title</h2>
				</div>

				<div class="swiper-container swiper-container_about">
					<div class="swiper-wrapper swiper-wrapper_about">


						<div class="swiper-slide swiper-slide_about" data-id="<?= $compt ?>">  

							<div class="swiper-slide_about__container">

								<div class="swiper-slide_about__container__first__image">

									<img src="https://dummyimage.com/600x400/000/fff" />

								</div>

								<div class="swiper-slide_about__container__second__image reverse">
									<img src="https://dummyimage.com/600x400/000/fff" />
								</div>



							</div>

						</div>

						<div class="swiper-slide swiper-slide_about" data-id="<?= $compt ?>">  
							
							<div class="swiper-slide_about__container">

								<div class="swiper-slide_about__container__first__image">

									<img src="https://dummyimage.com/600x400/000/fff" />

								</div>

								<div class="swiper-slide_about__container__second__image">
									<img src="https://dummyimage.com/600x400/000/fff" />
								</div>



							</div>

						</div>
							
					</div>

					
					 
												
				</div>

				<div class="about__slider__text">

					<div class="about__slider__text__paragraph">

						<?php 

						$compt = 0;

						if( have_rows('patchwork') ):

							while( have_rows('patchwork') ) : the_row();

							$compt++;
								$patchwork_text = get_sub_field('patchwork_text'); ?>

							<?php if ($compt == 1): ?>
								<p class="js__<?= $compt ?>__text slide__text__id text__active"  data-id="<?= $compt?>"><?= $patchwork_text ?></p>
							<?php else: ?>
							<p class="js__<?= $compt ?>__text slide__text__id"  data-id="<?= $compt?>"><?= $patchwork_text ?></p>

							<?php endif; ?>

							<?php	endwhile;
							else :
						endif; ?>
					</div>

					<div class="about__slider__text__button">

						<?php 

						$compt = 0;

						if( have_rows('patchwork') ):

							while( have_rows('patchwork') ) : the_row();

							$compt++;
								$patchwork_link = get_sub_field('patchwork_button_link');
								$patchwork_text = get_sub_field('patchwork_button_text'); ?>

							<?php if ($compt == 1): ?>
								<a href="<?= $patchwork_link ?>" class="button__anim js__<?= $compt ?>__button slide__button__id text__active " data-id="<?= $compt?>">
									<div class="button__anim__circle"></div>
									<div class="button__anim__text"><?= $patchwork_text ?></div>
								</a>
							<?php else: ?>
								<a href="<?= $patchwork_link ?>" class="button__anim js__<?= $compt ?>__button slide__button__id " data-id="<?= $compt?>">
									<div class="button__anim__circle"></div>
									<div class="button__anim__text"><?= $patchwork_text ?></div>
								</a>
							<?php endif; ?>

						<?php
							endwhile;
							else :
						endif; ?>
					</div>


					
					
				</div>
				<div class="swiper-button-next-svg"><?php include("inc/arrow-after.php")?></div>
					<div class="swiper-button-prev-svg"><?php include("inc/arrow-before.php")?></div> 
			</div>
			

	</section>
		<?php
	}
}

    