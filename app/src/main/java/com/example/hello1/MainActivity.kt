package com.example.hello1

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.GridLayoutManager
import com.example.hello1.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity(R.layout.activity_main) {
    lateinit var binding: ActivityMainBinding
    private val adapter = RectangleAdapter()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(R.layout.activity_main)
        initRCView()

    }

    private fun initRCView(){
        binding.apply {
            recyclerRectangle.layoutManager = GridLayoutManager(this@MainActivity, 3)
            recyclerRectangle.adapter = adapter
            addButton.setOnClickListener {
                adapter.addRectangle()
            }
            button2.setOnClickListener{
                adapter.addRectangle()
            }
        }
    }
}