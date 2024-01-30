package com.example.birdsidentifier

import android.content.Intent
import android.graphics.Bitmap
import android.media.ThumbnailUtils
import android.net.Uri
import android.os.Bundle
import android.provider.MediaStore
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.example.birdsidentifier.databinding.ActivityMainBinding
import com.example.birdsidentifier.ml.Model
import org.tensorflow.lite.DataType
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer
import java.io.IOException
import java.nio.ByteBuffer
import java.nio.ByteOrder

@Suppress("DEPRECATION")
class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private lateinit var loadPhotoButton: Button
    private lateinit var photoImageView: ImageView
    private lateinit var predictionTextView: TextView
    private lateinit var cameraButton: Button
    private val imageSize = 224

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        loadPhotoButton = binding.loadBirdPhoto
        photoImageView = binding.birdImageView
        predictionTextView = binding.prediction
        cameraButton = binding.takBirdPhoto


        loadPhotoButton.setOnClickListener {
            //Launch gallery to pick a photo for model
            val cameraIntent = Intent(Intent.ACTION_GET_CONTENT, MediaStore.Images.Media.EXTERNAL_CONTENT_URI)
            startActivityForResult(cameraIntent, 5)
        }

        cameraButton.setOnClickListener {
            // Launch camera to take a photo for model
            val cameraIntent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
            startActivityForResult(cameraIntent, 4)
        }
    }

    @Deprecated("Deprecated in Java")
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if(resultCode == RESULT_OK){
            if(requestCode == 4) run {
                var image = data?.extras?.get("data") as Bitmap
                val dimension = kotlin.math.min(image.width, image.height)
                //Resizing Bitmap
                image = ThumbnailUtils.extractThumbnail(image, dimension, dimension)
                photoImageView.setImageBitmap(image)
                image = Bitmap.createScaledBitmap(image, imageSize, imageSize, false)
                classifyImage(image)
            } else {
                val uri : Uri = data?.data!!
                var image : Bitmap? = null
                try{
                    image = MediaStore.Images.Media.getBitmap(this.contentResolver, uri)
                } catch (e : IOException){
                    e.printStackTrace()
                }
                photoImageView.setImageBitmap(image)
                image = image?.let { Bitmap.createScaledBitmap(it, imageSize, imageSize, false) }
                classifyImage(image)
            }
        }
        super.onActivityResult(requestCode, resultCode, data)
    }

    private fun classifyImage(image: Bitmap?) {
        if(image != null){
            val model = Model.newInstance(applicationContext)

            // Creates inputs for reference.
            val inputFeature0 = TensorBuffer.createFixedSize(intArrayOf(1, 224, 224, 3), DataType.FLOAT32)
            val byteBuffer : ByteBuffer = ByteBuffer.allocateDirect(4 * 3 * imageSize * imageSize)
            byteBuffer.order(ByteOrder.nativeOrder())
            val intValues = IntArray(imageSize * imageSize)
            image.getPixels(intValues, 0, image.width, 0, 0, image.width, image.height)
            var pixel = 0
            for (i in 0 until imageSize) {
                for (j in 0 until imageSize) {
                    val `val` = intValues[pixel++] // RGB
                    byteBuffer.putFloat((`val` shr 16 and 0xFF) * (1f / 1))
                    byteBuffer.putFloat((`val` shr 8 and 0xFF) * (1f / 1))
                    byteBuffer.putFloat((`val` and 0xFF) * (1f / 1))
                }
            }
            inputFeature0.loadBuffer(byteBuffer)

            // Runs model inference and gets result.
            val outputs = model.process(inputFeature0)
            val outputFeature0 = outputs.outputFeature0AsTensorBuffer

            val confidences = outputFeature0.floatArray
            // find the index of the class with the biggest confidence.
            var maxPos = 0
            var maxConfidence = 0f
            for (i in confidences.indices) {
                if (confidences[i] > maxConfidence) {
                    maxConfidence = confidences[i]
                    maxPos = i
                }
            }
            val birdNamesArray = arrayOf(
                "AMERICAN FLAMINGO",
                "BALD EAGLE",
                "CALIFORNIA GULL",
                "CROW",
                "EMPEROR PENGUIN",
                "EMU",
                "LONG-EARED OWL",
                "MALLARD DUCK",
                "OSTRICH",
                "PEACOCK",
                "ROCK DOVE",
                "SNOW GOOSE"
            )
            predictionTextView.text = birdNamesArray[maxPos]
            // Releases model resources if no longer used.
            model.close()
        }
    }
}
