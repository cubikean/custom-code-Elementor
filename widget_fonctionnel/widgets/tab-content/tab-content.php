<?php

namespace Elementor;

class Tab_Content extends Widget_Base
{

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
		return 'Tab Content';
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
		return 'eicon-editor-code';
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
				'label' => __('Tab Content', 'tab-content'),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);


		$repeater = new \Elementor\Repeater();

		$repeater->add_control(
			'ImageTab',
			[
				'label' => __('Icon de l\'onglet', 'tab-content'),
				'type' => \Elementor\Controls_Manager::MEDIA,

			]
		);


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
			'Content',
			[
				'label' => __('Contenu', 'tab-content'),
				'type' => \Elementor\Controls_Manager::WYSIWYG,
				'input_type' => 'wysiwyg',
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
			'Icon1',
			[
				'label' => __('Icon 1', 'tab-content'),
				'type' => \Elementor\Controls_Manager::MEDIA,

			]
		);

		$repeater->add_control(
			'Icon1Title',
			[
				'label' => __('Titre 1er icon', 'tab-content'),
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
				'label' => __('Titre 2er icon', 'tab-content'),
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
				'label' => __('Titre 3er icon', 'tab-content'),
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
				'label' => __('Titre 4er icon', 'tab-content'),
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
		// var_dump($settings['list']);


?>
		<div class="pc-tab">
			<?php if ($settings['list']) {
				$tabId = 2; ?>
				<input checked="checked" id="tab1" type="radio" name="pct" />
				<?php foreach ($settings['list'] as $item) { ?>
					<input id="tab<?= $tabId ?>" type="radio" name="pct" />
			<?php $tabId = $tabId + 1;
				}
			} ?>
			<nav>
				<ul>

					<?php if ($settings['list']) {
						$valueIncRender = 1; ?>
						<?php foreach ($settings['list'] as $index => $item) {

							// inline editing setup for TitleTab
							$repeater_setting_key_title_tab = $this->get_repeater_setting_key('TitleTab', 'list', $index);
							$this->add_inline_editing_attributes($repeater_setting_key_title_tab);

						?>
							<li class="tab<?= $valueIncRender ?>">
								<label for="tab<?= $valueIncRender ?>" class="image-icon">
									<img src="<?= $item['ImageTab']['url'] ?>" alt="" />
									<p <?php $this->print_render_attribute_string($repeater_setting_key_title_tab) ?>><?php $title_tab = $settings['list'][$index]['TitleTab'];
																														echo $title_tab ?> </p>
								</label>
							</li>
					<?php $valueIncRender = $valueIncRender + 1;
						}
					} ?>

				</ul>
			</nav>
			<section>

				<?php if ($settings['list']) {
					$valueIncRenderTab = 1; ?>
					<?php foreach ($settings['list'] as $index => $item) {

						// inline editing setup for TitleContent
						$repeater_setting_key_title_content = $this->get_repeater_setting_key('TitleContent', 'list', $index);
						$this->add_inline_editing_attributes($repeater_setting_key_title_content);

						// inline editing setup for Content
						$repeater_setting_key_content = $this->get_repeater_setting_key('Content', 'list', $index);
						$this->add_inline_editing_attributes($repeater_setting_key_content);

					?>
						<div class="tab tab<?= $valueIncRenderTab ?>">
							<div class="tab-container">
								<div class="tab-container_image">
									<img src="<?= $item['ImageContent']['url'] ?>" alt="" />
								</div>
								<div class="tab-container_content">
									<h2 <?php $this->print_render_attribute_string($repeater_setting_key_title_content) ?> class="tab-container_content_title">

										<?php $title = $settings['list'][$index]['TitleContent'];
										echo $title ?>

									</h2>
									<p <?php $this->print_render_attribute_string($repeater_setting_key_content) ?> class="tab-container_content_text">

										<?php $content = $settings['list'][$index]['Content'];
										echo $content ?>

									</p>
								</div>
								<div class="tab-container_icon">
									<?php if (!empty($item['Icon1']['url'])) { ?>
										<div class="tab-container_icon_image">
											<img src="<?php echo $item['Icon1']['url'] ?>" alt="" class="icon" />
											<p><?php echo $item['Icon1Title'] ?></p>
										</div>
									<?php } ?>
									<?php if (!empty($item['Icon2']['url'])) { ?>
										<div class="tab-container_icon_image">
											<img src="<?php echo $item['Icon2']['url'] ?>" alt="" class="icon" />
											<p><?php echo $item['Icon2Title'] ?></p>
										</div>
									<?php } ?>
									<?php if (!empty($item['Icon3']['url'])) { ?>
										<div class="tab-container_icon_image">
											<img src="<?php echo $item['Icon3']['url'] ?>" alt="" class="icon" />
											<p><?php echo $item['Icon3Title'] ?></p>
										</div>
									<?php } ?>
									<?php if (!empty($item['Icon4']['url'])) { ?>
										<div class="tab-container_icon_image">
											<img src="<?php echo $item['Icon4']['url'] ?>" alt="" class="icon" />
											<p><?php echo $item['Icon4Title'] ?></p>
										</div>
									<?php } ?>
								</div>
							</div>
						</div>
				<?php $valueIncRenderTab = $valueIncRenderTab + 1;
					}
				} ?>

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


				<div class="pc-tab">
					<# if ( settings.list ) { #>
						<# var tabId=2; #>
							<input checked="checked" id="tab1" type="radio" name="pct" />
							<# _.each( settings.list, function( item ) { #>
								<input id="tab{{ tabId }}" type="radio" name="pct" />
								<# tabId=tabId + 1; #>
									<# }); #>
										<# } #>
											<nav>
												<ul>
													<# if ( settings.list ) { #>
														<# var valueIncTemplate=1; #>
															<# _.each( settings.list, function( item ) { #>
																<li class="tab{{ valueIncTemplate }}">
																	<label for="tab{{ valueIncTemplate }}" class="image-icon">
																		<img src="{{ item.ImageTab.url }}" alt="" />
																		<p>{{{ item.TitleTab }}}</p>
																	</label>
																</li>
																<# valueIncTemplate=valueIncTemplate + 1; #>
																	<# }); #>
																		<# } #>

												</ul>
											</nav>

											<section>
												<# if ( settings.list ) { #>
													<# var valueIncTemplateSection=1 ;#>
														<# _.each( settings.list, function( item ) { #>

															<div class="tab tab{{ valueIncTemplateSection }}">
																<div class="tab-container">
																	<div class="tab-container_image">
																		<img src="{{ item.ImageContent.url }}" alt="" />
																	</div>
																	<div class="tab-container_content">
																		<h2 class="tab-container_content_title">
																			{{{ item.TitleContent }}}
																		</h2>
																		<p class="tab-container_content_text">
																			{{{ item.Content }}}
																		</p>
																	</div>
																	<div class="tab-container_icon">
																		<# if ( item.GalleryIcon ) { #>
																			<# _.each( item.GalleryIcon, function( image ) { #>
																				<div class="tab-container_icon_image"><img src="{{ image.url }}" alt="" class="icon" /></div>
																				<# }); #>
																					<# } #>
																	</div>
																</div>
															</div>
															<# valueIncTemplateSection=valueIncTemplateSection + 1 ;#>
																<# }); #>
																	<# } #>
											</section>
				</div>


		<?php
		}
	}
