# B30. Generate an AI-created image, applying an imperceptible watermark on it and then perform an image-to-image regeneration or editing process to make sure the watermark is detectable---the watermark survives.


For this activity, I generated an AI-created image and then applied an imperceptible watermark to it in order to test whether the hidden watermark could still be detected after the image went through an editing process. The purpose of this activity was to explore whether an invisible watermark can remain embedded in an image even after the image has been modified, which is important when thinking about image authenticity, provenance, and the resilience of hidden ownership or tracking information. I wanted this activity to directly match the instruction, so I made sure it included all three required parts: first generating the AI image, then embedding an invisible watermark into it, and finally performing an image editing step before testing whether the watermark was still detectable afterwards.

To carry this out, I first created an AI-generated image and saved it as the original input image. After that, I used a Python-based invisible watermarking library inside VS Code to embed a hidden text watermark into the image. This watermark was designed to be imperceptible, meaning it was not meant to be visibly noticeable when looking at the image normally. Once the watermarked version was created, I ran the extraction step to confirm that the watermark had been embedded successfully and could be detected in the watermarked image before any editing took place. This was an important part of the process, because it confirmed that the watermarking stage had worked properly before moving on to the next step.

After confirming that the watermark was present, I then performed an image editing process on the watermarked image. The purpose of this step was to simulate an image-to-image modification and then test whether the hidden watermark could still survive that change. Once the edited version had been produced, I ran the watermark detection step again on the edited image. The watermark was still detectable after the edit, which showed that the invisible watermark had survived the image modification process. This was the key result required by the activity, because it demonstrated that the watermark was not only embedded successfully, but also remained recoverable even after the image had been altered.

Overall, I found this activity very meaningful because it gave me a practical understanding of how hidden watermarking works and why robustness matters. It showed that an imperceptible watermark can be used in a way that does not visibly change the image for normal viewing, while still remaining detectable after a later editing step. This directly fulfilled the instruction of the activity, since I generated an AI image, applied an imperceptible watermark to it, carried out an editing process, and then verified that the watermark survived and was still detectable afterwards.





![Tailgating example](B30-image-created.png)


**Figure: AI image generated**




![Tailgating example](B30-output proof.png)

**Figure: Full output of this activity**





 

*Python Script Evidence on Github*



*Edited Image Evidence on Github*



*Watermarked Image Evidence on Github*
