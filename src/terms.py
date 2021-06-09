from pywebio.output import put_markdown
from pywebio.platform import seo
from pywebio.session import run_js

from src.utils.content import footer, header


@seo('Burplist', 'Beer prices at your fingertips')
def terms() -> None:
    run_js(header)
    run_js(footer)

    put_markdown(r"""
    Terms of Service
    ================

    Last revised on 1 May 2021

    ### The Gist

    If you use Burplist, please use it responsibly.

    The Terms of Service, Burplist itself, and our prices can change at any time. While the service is currently free of charge, we'll warn you 30 days in advance of any price changes. We'll try to warn you about major changes to the Terms of Service, but we make no guarantees.

    That's the basic idea, but You must read through the entire Terms of Service below and agree with all the details before You use any of our sites (whether or not you have created an account).

    ### Your Agreement with Burplist

    Your use of the Burplist service is governed by this agreement (the "Terms"). "Burplist" means Burplist Inc. The "Service" means the services Burplist makes available include our web site (https://burplist.me), our blog, our API, and any other software, sites, and services offered by Burplist in connection to any of those. "Content" means all content generated by Burplist on your behalf (including metric data).

    In order to use the Service, You (the "Customer", "You", or "Your") must first agree to the Terms. You understand and agree that Burplist will treat Your use of the Service as acceptance of the Terms from that point onwards.

    Burplist may make changes to the Terms from time to time. You may reject the changes by not using this Service. You understand and agree that if You use the Service after the date on which the Terms have changed, Burplist will treat Your use as acceptance of the updated Terms.

    If you have any question about the Terms, please contact us at hello@burplist.me.

    ### Use of the Service

    * Your use of the Service must comply with all applicable laws, regulations and ordinances.
    * You agree to not engage in any activity that interferes with or disrupts the Service.
    * Burplist reserves the right to enforce quotas and usage limits (to any resources, including the API) at its sole discretion, with or without notice, which may result in Burplist disabling or throttling your usage of the Service for any amount of time.

    ### Service Policies and Privacy

    The Service shall be subject to the privacy policy for the Service available at privacy policy. You agree to the use of Your data in accordance with Burplist's privacy policies.

    ### Ideas and Feedback

    You may choose to or we may invite You to submit comments or ideas about the Service, including but not limited to ideas about improving the Service or our products ("Ideas"). By submitting any Idea, You agree that Your disclosure is unsolicited and without restriction and will not place Burplist under any fiduciary or other obligation, and that we are free to use the Idea without any additional compensation to You, and/or to disclose the Idea on a non-confidential basis or otherwise to anyone.

    ### Modification of the Service

    * You acknowledge and agree that the Service may change from time to time without prior notice to You.
    * Changes include, without limitation, changes to fee and payment policies, security patches, added or removed functionality, and other enhancements or restrictions.
    * Burplist shall not be liable to you or to any third party for any modification, price change, suspension or discontinuance of the Service.

    ### External Resources

    The Services may include hyperlinks to other web sites or content or resources or email content. You acknowledge and agree that Burplist is not responsible for the availability of any such external sites or resources, and does not endorse any advertising, products or other materials on or available from such web sites or resources.

    ### License from Burplist and Restrictions

    Burplist gives You a personal, worldwide, royalty-free, non-assignable and non-exclusive license to use the software provided to You by Burplist as part of the Service as provided to You by Burplist. This license is for the sole purpose of enabling You to use and enjoy the benefit of the Service as provided by Burplist, in the manner permitted by the Terms.

    You may not (and You may not permit anyone else to): (a) copy, modify, create a derivative work of, reverse engineer, decompile or otherwise attempt to extract the source code of the Service or any part thereof, unless this is expressly permitted or required by law, or unless You have been specifically told that You may do so by Burplist, in writing (e.g., through an open source software license); or (b) attempt to disable or circumvent any security mechanisms used by the Service.

    Open source software licenses for components of the Service released under an open source license constitute separate written agreements. To the limited extent that the open source software licenses expressly supersede these Terms, the open source licenses govern Your agreement with Burplist for the use of the components of the Service released under an open source license.

    ### Exclusion of warranties

    * You expressly understand and agree that your use of the service is at your sole risk and that the service is provided "as is" and "as available.".
    * You agree that Burplist has no responsibility or liability for the deletion or failure to store any Content and other communications maintained or transmitted through use of the Service. You further acknowledge that You are solely responsible for your own use of information on Burplist.
    * Burplist does not warrant to you that: (a) your use of the service will meet your requirements, (b) your use of the service will be uninterrupted, timely, secure or free from error, (c) the results or data provided by the Service will be accurate, (d) the quality of the service will meet your expectations and (e) any errors in the Service will be fixed.

    ### Limitation of liability

    You expressly understand and agree that Burplist, its subsidiaries and affiliates, and its licensors shall not be liable to you for any direct, indirect, incidental, special consequential or exemplary damages which may be incurred by you, however caused and under any theory of liability. This shall include, but not be limited to, any loss of profit (whether incurred directly or indirectly), any loss of goodwill or business reputation, any loss of data suffered, cost of procurement of substitute goods or services, or other intangible loss (whether or not Burplist has been advised of or should have been aware of the possibility of any such losses arising).

    ### Indemnification

    You agree to hold harmless and indemnify Burplist, and its subsidiaries, affiliates, officers, agents, employees, advertisers, licensors, suppliers or partners (collectively "Burplist and Partners") from and against any third party claim arising from or in any way related to (a) Your breach of the Terms, (b) Your use of the Service, (c) Your violation of applicable laws, rules or regulations in connection with the Service, or (d) Your Customer Source Code, including any liability or expense arising from all claims, losses, damages (actual and consequential), suits, judgments, litigation costs and attorneys' fees, of every kind and nature. In such a case, Burplist will provide You with written notice of such claim, suit or action.

    ### General Legal Terms

    The Terms constitute the whole legal agreement between You and Burplist and govern Your use of the Service and completely replace any prior agreements between You and Burplist in relation to the Service.

    You agree that if Burplist does not exercise or enforce any legal right or remedy which is contained in the Terms (or which Burplist has the benefit of under any applicable law), this will not be taken to be a formal waiver of Burplist's rights and that those rights or remedies will still be available to Burplist.

    Burplist shall not be liable for failing or delaying performance of its obligations resulting from any condition beyond its reasonable control, including but not limited to, governmental action, acts of terrorism, earthquake, fire, flood or other acts of God, labor conditions, power failures, and Internet disturbances.
    """, lstrip=True)
