package com.example.first_vk_app

import android.content.res.Configuration
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.first_vk_app.databinding.ActivityMainBinding


class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        supportFragmentManager
            .beginTransaction()
            .replace(R.id.fragment1, GalleryFragment.newInstance())
            .commit()


    }

//
//    override fun onSaveInstanceState(outState: Bundle) {
//        outState.run {
//            outState.putInt("COUNT_RECT", binding.recyclerRectangle.adapter!!.itemCount)
//        }
//        super.onSaveInstanceState(outState)
//    }
}