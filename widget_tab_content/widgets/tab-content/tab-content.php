<?php

namespace Elementor;

class Tab_Content extends Widget_Base
{

	// public function __construct($data = [], $args = null) {
	// 	parent::__construct($data, $args);
	
	// 	wp_register_script( 'tab-content', plugins_url( 'js/tab-content.js', __FILE__ ), [ 'jquery' ], '1.0.0', true );
	// }
	
	// public function get_script_depends() {
	// 	return [ 'tab-content' ];
	// }
	 
	/**
	 * Get widget name.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return string Widget name.
	 */
	public function get_name()
	{
		return 'tab-content';
	}

	/**
	 * Get widget title.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return string Widget title.
	 */
	public function get_title()
	{
		return 'Skydrone Produit';
	}

	/**
	 * Get widget icon.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return string Widget icon.
	 */
	public function get_icon()
	{
		return 'eicon-thumbnails-down';
	}

	/**
	 * Get widget categories.
	 * @since 1.0.0
	 * @access public
	 *
	 * @return array Widget categories.
	 */
	public function get_categories()
	{
		return ['basic'];
	}

	/**
	 * Register widget controls.
	 * @since 1.0.0
	 * @access protected
	 */
	protected function _register_controls()
	{

		/**
		 *  Here you can add your controls. The controls below are only examples.
		 *  Check this: https://developers.elementor.com/elementor-controls/
		 *
		 **/


		$this->start_controls_section(
			'content_section',
			[
				'label' => __('Skydrone Produit', 'tab-content'),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);


		$repeater = new \Elementor\Repeater();

		


		$repeater->add_control(
			'TitleTab',
			[
				'label' => __('Titre de l\'onglet', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);

		$repeater->add_control(
			'TitleContent',
			[
				'label' => __('Titre du contenu', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);

		$repeater->add_control(
			'ImageContent',
			[
				'label' => __('Image du contenu', 'tab-content'),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'dynamic' => [
					'active' => true,
				],

			]
		);
		
		$repeater->add_control(
			'IconContent',
			[
				'label' => __('Icon du contenu', 'tab-content'),
				'type' => \Elementor\Controls_Manager::MEDIA,

			]
		);

		$repeater->add_control(
			'Content',
			[
				'label' => __('Contenu', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXTAREA,
				'input_type' => 'wysiwyg',
				'dynamic' => [
					'active' => true,
				],
			]
		);



		$repeater->add_control(
			'Icon1',
			[
				'label' => __('Icon 1', 'tab-content'),
				'type' => \Elementor\Controls_Manager::MEDIA,

			]
		);

		$repeater->add_control(
			'Icon1Title',
			[
				'label' => __('Titre', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);
		$repeater->add_control(
			'Icon1SubTitle',
			[
				'label' => __('Sous-titre', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);

		$repeater->add_control(
			'Icon2',
			[
				'label' => __('Icon 2', 'tab-content'),
				'type' => \Elementor\Controls_Manager::MEDIA,

			]
		);

		$repeater->add_control(
			'Icon2Title',
			[
				'label' => __('Titre', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);
		$repeater->add_control(
			'Icon2SubTitle',
			[
				'label' => __('Sous-titre', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);

		$repeater->add_control(
			'Icon3',
			[
				'label' => __('Icon 3', 'tab-content'),
				'type' => \Elementor\Controls_Manager::MEDIA,

			]
		);

		$repeater->add_control(
			'Icon3Title',
			[
				'label' => __('Titre', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);
		$repeater->add_control(
			'Icon3SubTitle',
			[
				'label' => __('Sous-titre', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);

		$repeater->add_control(
			'Icon4',
			[
				'label' => __('Icon 4', 'tab-content'),
				'type' => \Elementor\Controls_Manager::MEDIA,

			]
		);

		$repeater->add_control(
			'Icon4Title',
			[
				'label' => __('Titre', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);
		$repeater->add_control(
			'Icon4SubTitle',
			[
				'label' => __('Sous-titre', 'tab-content'),
				'type' => \Elementor\Controls_Manager::TEXT,
				'input_type' => 'text',
				'dynamic' => [
					'active' => true,
				],
			]
		);



		$this->add_control(
			'list',
			[
				'label' => esc_html__('Onglet personnalisable', 'tab-content'),
				'type' => \Elementor\Controls_Manager::REPEATER,
				'fields' => $repeater->get_controls(),
				'default' => [
					[
						'TitleTab' => esc_html__('Titre de l\'onglet ...', 'tab-content'),
						'TitleContent' => esc_html__('Titre de votre contenu...', 'tab-content'),
						'Content' => esc_html__('Votre contenu...', 'tab-content'),
					],
					[
						'TitleTab' => esc_html__('Titre de l\'onglet ...', 'tab-content'),
						'TitleContent' => esc_html__('Titre de votre contenu...', 'tab-content'),
						'Content' => esc_html__('Votre contenu...', 'tab-content'),
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
	protected function render()
	{

		$settings = $this->get_settings_for_display();

		/**
		 *  Here you can output your control data and build your content.
		 **/

?>

		<div class="bk-tab">
			<div class="bk-tab__nav">
				<?php if ($settings['list']) { ?>
					<?php $count = 1 ?>

					<?php foreach ($settings['list'] as $index => $item) { ?>
						<button class="bk-tab__nav__item <?php if ($count === 1) { echo 'bk-tab__nav__item--active';} ?> posItem"><?php echo $item['TitleTab'] ?></button>
				<?php $count = $count + 1;
					}
				} ?>

				<div class="bk-tab__nav__bar"></div>

				<select class="bk-tab__nav__select" name="bk-tab" id="bk-tab">
					<?php if ($settings['list']) {
						$optVal = 1 ?>
						<?php foreach ($settings['list'] as $item) { ?>
							<option value="<?= $optVal ?>"><?= $item['TitleTab'] ?></option>
					<?php $optVal = $optVal + 1;
						}
					} ?>
				</select>

			</div>

			<section class="bk-tab__container">
				<div class="bk-tab__container__top">
					<?php if ($settings['list']) { ?>
						<?php $count = 1 ?>
						<?php foreach ($settings['list'] as $index => $item) {?>

							<div class="bk-tab__container__top__single <?php if ($count != 1) { echo'is-disabled'; } ?>">
								<div class="bk-tab__container__top__single__image">
									<img src="<?= $item['ImageContent']['url'] ?>" alt="" />
								</div>
								<div class="bk-tab__container__top__single__content">
									<img class="bk-tab__container__top__single__content__image" src="<?= $item['IconContent']['url'] ?>" alt="">
									<h2 class="bk-tab__container__top__single__content__title"><?php echo $item['TitleContent'] ?></h2>
									<p class="bk-tab__container__top__single__content__text"><?= $item['Content'] ?></p>
									
								</div>
							</div>
					<?php $count = $count + 1;
						}
					} ?>
				</div>

				<div class="bk-tab__container__icon">
					<?php if ($settings['list']) { ?>
						<?php $count = 1 ?>
						<?php foreach ($settings['list'] as $index => $item) { ?>

							<div class="bk-tab__container__icon__single <?php if ($count != 1) { echo 'is-disabled'; } ?>">
								<?php if (!empty($item['Icon1']['url'])) { ?>
									<div class="bk-tab__container__icon__single__content">
										<img src="<?php echo $item['Icon1']['url'] ?>" alt="" class="icon" />
										<h3><?php echo $item['Icon1Title'] ?></h3>
										<p><?php echo $item['Icon1SubTitle'] ?></p>
									</div>
								<?php } ?>
								<?php if (!empty($item['Icon2']['url'])) { ?>
									<div class="bk-tab__container__icon__single__content">
										<img src="<?php echo $item['Icon2']['url'] ?>" alt="" class="icon" />
										<h3><?php echo $item['Icon2Title'] ?></h3>
										<p><?php echo $item['Icon2SubTitle'] ?></p>
									</div>
								<?php } ?>
								<?php if (!empty($item['Icon3']['url'])) { ?>
									<div class="bk-tab__container__icon__single__content">
										<img src="<?php echo $item['Icon3']['url'] ?>" alt="" class="icon" />
										<h3><?php echo $item['Icon3Title'] ?></h3>
										<p><?php echo $item['Icon3SubTitle'] ?></p>
									</div>
								<?php } ?>
								<?php if (!empty($item['Icon4']['url'])) { ?>
									<div class="bk-tab__container__icon__single__content">
										<img src="<?php echo $item['Icon4']['url'] ?>" alt="" class="icon" />
										<h3><?php echo $item['Icon4Title'] ?></h3>
										<p><?php echo $item['Icon4SubTitle'] ?></p>
									</div>
								<?php } ?>
							</div>
					<?php $count = $count + 1;
						}
					} ?>
				</div>
			</section>
		</div>
	<?php
	}

	/**
	 * Written as a Backbone JavaScript template and used to generate the live preview.
	 * With JS templates we don’t really need to retrieve the data using a special function, its done by Elementor for us.
	 * The data from the controls stored in the settings variable.
	 */
	protected function content_template()
	{
	?>
	

<div class="bk-tab">
  <div class="bk-tab__nav">
    <# if ( settings.list ) { 
      var count = 1; 
      _.each( settings.list, function( item, index ) { 
        if ( count === 1 ) { #>
          <button class="bk-tab__nav__item tab__nav__item--active posItem">{{{ item.TitleTab }}}</button>
        <# } else { #>
          <button class="bk-tab__nav__item posItem">{{{ item.TitleTab }}}</button>
        <# } #>
        <# count = count + 1 #>
      <# }); #>
    <# } #>
    <div class="bk-tab__nav__bar"></div>
    <select class="bk-tab__nav__select" name="bk-tab" id="bk-tab">
      <# if ( settings.list ) { 
        var optVal = 1; 
        _.each( settings.list, function( item, index ) { #>
          <option value="{{optVal}}">{{{ item.TitleTab }}}</option>
          <# optVal = optVal + 1 #>
        <# }); #>
      <# } #>
    </select>
  </div>
  <section class="bk-tab__container">
    <div class="bk-tab__container__top">
      <# if ( settings.list ) { 
        var countD = 1; 
        _.each( settings.list, function( item, index ) { 
          if ( countD === 1 ) { #>
            <div class="bk-tab__container__top__single">
          <# } else { #>
            <div class="bk-tab__container__top__single is-disabled">
          <# } #>
            <div class="bk-tab__container__top__single__image">
              <img src="{{ item.ImageContent.url }}" alt="" />
            </div>
            <div class="bk-tab__container__top__single__content">
			  <img class="bk-tab__container__top__single__content__image" src="{{ item.IconContent.url }}" alt="">

              <h2 class="bk-tab__container__top__single__content__title">
                {{{ item.TitleContent }}}
              </h2>
              <p class="bk-tab__container__top__single__content__text">
                {{{ item.Content }}}
              </p>
            </div>
          </div>
          <# countD = countD + 1; #>
        <# }); #>
      <# } #>
    </div>
        <div class="bk-tab__container__icon">
            <# if ( settings.list ) { #>
                <# var countD = 1 ;#>
                    <# _.each( settings.list, function( item, index ) { 
                        if(countD === 1) { #>
							<div class="bk-tab__container__icon__single">
								<# if ( ! _.isEmpty( item.Icon1.url ) ) { #> 
									<div class="bk-tab__container__icon__single__image">
										<div class="bk-tab__container__icon__single__content">
											<img src="{{ item.Icon1.url }}" alt="" class="icon" />
											<h3>{{{ item.Icon1Title }}}</h3>
											<p>{{{ item.Icon1SubTitle }}}</p>
										</div>
									</div>
								<# } #>
								<# if ( ! _.isEmpty( item.Icon2.url ) ) { #> 
									<div class="bk-tab__container__icon__single__image">
										<div class="bk-tab__container__icon__single__content">
											<img src="{{ item.Icon2.url }}" alt="" class="icon" />
											<h3>{{{ item.Icon2Title }}}</h3>
											<p>{{{ item.Icon2SubTitle }}}</p>
										</div>
									</div>
								<# } #>
								<# if ( ! _.isEmpty( item.Icon3.url ) ) { #> 
									<div class="bk-tab__container__icon__single__image">
										<div class="bk-tab__container__icon__single__content">
											<img src="{{ item.Icon3.url }}" alt="" class="icon" />
											<h3>{{{ item.Icon3Title }}}</h3>
											<p>{{{ item.Icon3SubTitle }}}</p>
										</div>
									</div>
								<# } #>
								<# if ( ! _.isEmpty( item.Icon4.url ) ) { #> 
									<div class="bk-tab__container__icon__single__image">
										<div class="bk-tab__container__icon__single__content">
											<img src="{{ item.Icon4.url }}" alt="" class="icon" />
											<h3>{{{ item.Icon4Title }}}</h3>
											<p>{{{ item.Icon4SubTitle }}}</p>
										</div>
									</div>
								<# } #>
							</div>
                        <# } else { #>
							<div class="bk-tab__container__icon__single is-disabled">
								<# if ( ! _.isEmpty( item.Icon1.url ) ) { #> 
									<div class="bk-tab__container__icon__single__image">
										<div class="bk-tab__container__icon__single__content">
											<img src="{{ item.Icon1.url }}" alt="" class="icon" />
											<h3>{{{ item.Icon1Title }}}</h3>
											<p>{{{ item.Icon1SubTitle }}}</p>
										</div>
									</div>
								<# } #>
								<# if ( ! _.isEmpty( item.Icon2.url ) ) { #> 
									<div class="bk-tab__container__icon__single__image">
										<div class="bk-tab__container__icon__single__content">
											<img src="{{ item.Icon2.url }}" alt="" class="icon" />
											<h3>{{{ item.Icon2Title }}}</h3>
											<p>{{{ item.Icon2SubTitle }}}</p>
										</div>
									</div>
								<# } #>
								<# if ( ! _.isEmpty( item.Icon3.url ) ) { #> 
									<div class="bk-tab__container__icon__single__image">
										<div class="bk-tab__container__icon__single__content">
											<img src="{{ item.Icon3.url }}" alt="" class="icon" />
											<h3>{{{ item.Icon3Title }}}</h3>
											<p>{{{ item.Icon3SubTitle }}}</p>
										</div>
									</div>
								<# } #>
								<# if ( ! _.isEmpty( item.Icon4.url ) ) { #> 
									<div class="bk-tab__container__icon__single__image">
										<div class="bk-tab__container__icon__single__content">
											<img src="{{ item.Icon4.url }}" alt="" class="icon" />
											<h3>{{{ item.Icon4Title }}}</h3>
											<p>{{{ item.Icon4SubTitle }}}</p>
										</div>
									</div>
								<# } #>
							</div>
							<# } #>
                        <# countD = countD + 1 ;#>
                    <# }); #>
            <# } #>
        </div>
	</section>
</div>
<?php
	}
	
}
