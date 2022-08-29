import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# import pandas as pd

# change these as per use
your_email = "info@ddsbd.org"
your_password = "}W(Y0amI)?*4"

# recipient email
email = "risulislam089@gmail.com"

# establishing connection with gmail
server = smtplib.SMTP_SSL("server128.web-hosting.com", 465)
server.ehlo()
server.login(your_email, your_password)

# the message to be emailed
html = """\
		<!DOCTYPE html>
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<style>
		* {
			box-sizing: border-box;
		}

		body {
			margin: 0;
			padding: 0;
		}

		a[x-apple-data-detectors] {
			color: inherit !important;
			text-decoration: inherit !important;
		}

		#MessageViewBody a {
			color: inherit;
			text-decoration: none;
		}

		p {
			line-height: inherit
		}

		.desktop_hide,
		.desktop_hide table {
			mso-hide: all;
			display: none;
			max-height: 0px;
			overflow: hidden;
		}

		@media (max-width:660px) {
			.desktop_hide table.icons-inner {
				display: inline-block !important;
			}

			.icons-inner {
				text-align: center;
			}

			.icons-inner td {
				margin: 0 auto;
			}

			.fullMobileWidth,
			.row-content {
				width: 100% !important;
			}

			.mobile_hide {
				display: none;
			}

			.stack .column {
				width: 100%;
				display: block;
			}

			.mobile_hide {
				min-height: 0;
				max-height: 0;
				max-width: 0;
				overflow: hidden;
				font-size: 0px;
			}

			.desktop_hide,
			.desktop_hide table {
				display: table !important;
				max-height: none !important;
			}
		}
	</style>
</head>

<body style="background-color: #f8f8f9; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f8f8f9;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1aa19c;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; background-color: #1aa19c; width: 640px;" width="640">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="divider_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 4px solid #1AA19C;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fff; color: #000000; width: 640px;" width="640">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:40px;padding-right:40px;width:100%;">
																<div class="alignment" align="center" style="line-height:10px"><img class="fullMobileWidth" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/859729_843820/%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A5%E0%A6%AE-%E0%A6%AE%E0%A7%8C%E0%A6%B8%E0%A7%81%E0%A6%AE-.jpg" style="display: block; height: auto; border: 0; width: 560px; max-width: 100%;" width="560" alt="I'm an image" title="I'm an image"></div>
															</td>
														</tr>
													</table>
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class="txtTinyMce-wrapper" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #555555; line-height: 1.2; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;">
																		<p style="margin: 0; font-size: 16px; text-align: center;"><span style="font-size:20px;"><strong>অভিনন্দন!!</strong></span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class="txtTinyMce-wrapper" style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 18px; color: #555555; line-height: 1.5;">
																		<p style="margin: 0; font-size: 14px; text-align: left;"><strong><span style="font-size:15px;">“<span style="color:#066c54;">মেগা কুইজ প্রতিযোগিতা ১ম মৌসুম</span>” নিবন্ধন করার জন্য অসংখ্য ধন্যবাদ। আপনি সফল ভাবে নিবন্ধন সম্পন্ন করতে পেরেছেন।</span></strong></p>
																		<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 18px;">&nbsp;</p>
																		<p style="margin: 0; text-align: left; mso-line-height-alt: 21px;"><span style="font-size:14px;"><strong>কুইজের নিয়মাবলী:</strong></span></p>
																		<ul style="text-align: left; line-height: 1.5; mso-line-height-alt: 21px;">
																			<li><strong>মোট&nbsp;<span style="font-size:13px;">৩০</span>&nbsp;টি MCQ প্রশ্ন থাকবে।</strong></li>
																			<li><strong>মোট নাম্বার থাকবে&nbsp;<span style="font-size:13px;">৩০</span>।</strong></li>
																			<li><strong>সময় থাকবে&nbsp;<span style="font-size:13px;">৩০</span> মিনিট।</strong></li>
																			<li><strong>অনুগ্রহ পূর্ব ডিডিএস আইডি সংরক্ষণ করে রাখুন।&nbsp;<br></strong></li>
																			<li><strong>আপানার নাম এবং ডিডিএস আইডি দ্বারা কুইজ প্রতিযোগিতায় অংশগ্রহন করতে পারবেন।</strong></li>
																		</ul>
																		<p style="margin: 0; font-size: 14px; text-align: left;"><strong><span style="font-size:15px;">আমাদের ইভেন্ট পেইজে যুক্ত থাকার বিশেষ পরামর্শ রইলো, তাহলে কুইজের সময় ভুলে যাওয়া বা সর্বশেষ তথ্য সহজেই আপনাদের কাছে পৌঁছাবে।<br></span></strong></p>
																		<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 18px;">&nbsp;</p>
																		<p style="margin: 0; font-size: 14px; text-align: left;"><strong><span style="font-size:15px;">ইভেন্ট পেইজ: <span style="color:#03a2f8;"><a href="https://fb.me/e/1HalYusog" target="_blank" style="text-decoration:underline;color:#03a2f8;" rel="noopener">Facebook Event</a></span></span></strong></p>
																		<p style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 18px;">&nbsp;</p>
																		<p style="margin: 0; font-size: 14px; text-align: left;"><strong><span style="font-size:15px;">কুইজ অনুষ্ঠিত হবে <span style="color:#e30000;">১৫-১০-২০২২</span> তারিখ সন্ধ্যা <span style="color:#e30000;">৭</span> টায় ডিডিএস ওয়েবসাইটে।</span></strong></p>
																		<p style="margin: 0; font-size: 14px; text-align: left;"><strong>কুইজ লিংকঃ<span style="color:#066c54;"> <a href="https://ddsbd.org/mega-quiz-2022-session-1" target="_blank" style="text-decoration:underline;color:#066c54;" rel="noopener">Quiz link</a></span></strong></p>
																		<p style="margin: 0; font-size: 14px; text-align: justify; mso-line-height-alt: 18px;">&nbsp;</p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-3" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; background-color: #f3fafa; width: 640px;" width="640">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; border-left: 30px solid #FFFFFF; border-right: 30px solid #FFFFFF; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-bottom: 0px;">
													<table class="divider_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 4px solid #1AA19C;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:5px;padding-left:10px;padding-right:10px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class="txtTinyMce-wrapper" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #555555; line-height: 1.2; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;">
																		<p style="margin: 0; font-size: 16px; text-align: center;"><span style="color:#029153;"><strong><span style="font-size:20px;"><span style="color:#066c54;">DDS ID:</span> MQ1S0001</span></strong></span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-4" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fff; color: #000000; width: 640px;" width="640">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="text_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class="txtTinyMce-wrapper" style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 18px; color: #555555; line-height: 1.5;">
																		<p style="margin: 0; font-size: 14px; text-align: justify; mso-line-height-alt: 21px;"><span style="font-size:14px;"><strong>যেকোনো প্রয়োজনে:</strong></span></p>
																		<p style="margin: 0; font-size: 14px; text-align: justify; mso-line-height-alt: 21px;"><span style="font-size:14px;">ডিসেন্ট ড্রিমার্স সোসাইটি ফেসবুক পেজ: <a href="https://www.facebook.com/ddsbd.org" target="_blank" style="text-decoration: underline;" rel="noopener">Decent Dreamers Society</a></span></p>
																		<p style="margin: 0; font-size: 14px; text-align: justify; mso-line-height-alt: 21px;"><span style="font-size:14px;">ডিসেন্ট ড্রিমার্স সোসাইটি ফেসবুক গ্রুপ: <a href="https://www.facebook.com/groups/ddsbd.org" target="_blank" style="text-decoration: underline;" rel="noopener">Decent Dreamers Society</a></span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-5" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; background-color: #f5f5f5; width: 640px;" width="640">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="divider_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 4px solid #1AA19C;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="image_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-top:40px;width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px"><a href="https://www.ddsbd.org" target="_blank" style="outline:none" tabindex="-1"><img src="https://ddsbd.org/wp-content/uploads/2021/07/Logo-DDS-White-01.png" style="display: block; height: auto; border: 0; width: 224px; max-width: 100%;" width="224" alt="Alternate text" title="Alternate text"></a></div>
															</td>
														</tr>
													</table>
													<table class="divider_block block-3" width="100%" border="0" cellpadding="5" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 3px solid #37586D;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="social_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="text-align:center;padding-right:0px;padding-left:0px;">
																<div class="alignment" style="text-align:center;">
																	<table class="social-table" width="108px" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;">
																		<tr>
																			<td style="padding:0 2px 0 2px;"><a href="https://www.facebook.com/ddsbd.org" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/colored/facebook@2x.png" width="32" height="32" alt="Facebook" title="facebook" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 2px 0 2px;"><a href="https://www.twitter.com/ddsbd_org" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/colored/twitter@2x.png" width="32" height="32" alt="Twitter" title="twitter" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 2px 0 2px;"><a href="https://www.instagram.com/ddsbd_org" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/colored/instagram@2x.png" width="32" height="32" alt="Instagram" title="instagram" style="display: block; height: auto; border: 0;"></a></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:30px;padding-left:40px;padding-right:40px;padding-top:20px;">
																<div style="font-family: sans-serif">
																	<div class="txtTinyMce-wrapper" style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #555555; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; text-align: left;"><span style="color:#95979c;font-size:13px;">DDSBD Copyright © 2022</span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					
</body>

</html>
"""

# Eamil Content
msg = MIMEMultipart('alternative')
msg['Subject'] = "Your DDS Mega Quiz Event Session- 1 Registration Successfully"
msg['From'] = your_email
msg['To'] = email

body = MIMEText(html, 'html')
msg.attach(body)

# sending the email
server.sendmail(your_email, email, msg.as_string())

# close the smtp server
server.close()
print("email send success")