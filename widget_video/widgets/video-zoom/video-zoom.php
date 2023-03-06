<?php
namespace Elementor;

class Video_Zoom extends Widget_Base {

	/**
	 * Get widget name.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return string Widget name.
	 */
	public function get_name() {
		return 'video-zoom';
	}

	/**
	 * Get widget title.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return string Widget title.
	 */
	public function get_title() {
		return 'Video zoom';
	}

	/**
	 * Get widget icon.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return string Widget icon.
	 */
	public function get_icon() {
		return 'eicon-video-camera';
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
				'label' => __( 'Video zoom', 'video-zoom' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);

		$this->end_controls_section();
		$this->start_controls_section(
			'content_section',
			[
				'label' => __( 'Video zoom', 'video-zoom' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);

		$this->add_control(
			'textVideo',
			[
				'label' => __( 'Texte vidéo', 'video-zoom' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text'
			]
		);      

		$this->add_control(
			'video',
			[
				'label' => __( 'Vidéo', 'video-zoom' ),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'default' => [
					'url' => \Elementor\Utils::get_placeholder_image_src(),
				],
			]
		);      

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
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
 
  <body>
    <div class="container-video">
      <h1>coucou les loulous</h1>
      <!-- <img src="https://via.placeholder.com/850" alt="" /> -->

      <div class="spacer"></div>
    </div>
    <div class="spacer"></div>

    <div class="container-video">
      <video autoplay muted playsinline loop >
        <source src="<?php echo $settings['video']['url'] ?>" type="video/mp4" />
      </video>
      <div class="bottomVideoBlur"></div>
      <h2 class="absolText"><?php echo $settings['textVideo'] ?></h2>
    </div>

    <div class="container-video section-color">
      <div class="spacer"></div>
      <h2>A plus tout le monde !</h2>
      <div class="spacer"></div>
      <div class="spacer"></div>
      <div class="spacer"></div>
      <div class="spacer"></div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/ScrollTrigger.min.js"></script>
  </body>
</html>

 <?php

	}

	/**
	 * Written as a Backbone JavaScript template and used to generate the live preview.
	 * With JS templates we don’t really need to retrieve the data using a special function, its done by Elementor for us.
	 * The data from the controls stored in the settings variable.
	 */
	protected function _content_template() {
		?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
 
  <body>
    <div class="container-video">
      <h1>coucou les loulous</h1>
      <!-- <img src="https://via.placeholder.com/850" alt="" /> -->

      <div class="spacer"></div>
    </div>
    <div class="spacer"></div>

    <div class="container-video">
      <video autoplay muted playsinline loop >
        <source src="{{ settings.video.url }}" type="video/mp4" />
      </video>
      <div class="bottomVideoBlur"></div>
      <h2 class="absolText">{{{ settings.textVideo }}}</h2>
    </div>

    <div class="container-video section-color">
      <div class="spacer"></div>
      <h2>A plus tout le monde !</h2>
      <div class="spacer"></div>
      <div class="spacer"></div>
      <div class="spacer"></div>
      <div class="spacer"></div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/ScrollTrigger.min.js"></script>
  </body>
</html>

		<?php
	}
}

    