package com.example.first_vk_app

import android.content.res.Configuration
import androidx.lifecycle.ViewModelProvider
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.viewModels
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.first_vk_app.databinding.FragmentGalleryBinding

class GalleryFragment : Fragment() {

    companion object {
        fun newInstance() = GalleryFragment()
    }

    private val viewModel: GalleryViewModel by viewModels()
    private lateinit var binding: FragmentGalleryBinding

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentGalleryBinding.inflate(inflater)
        return binding.root
    }

    @Deprecated("Deprecated in Java")
    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)

        // TODO: Use the ViewModel
    }



    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val layoutManager: RecyclerView.LayoutManager =
            if (resources.configuration.orientation == Configuration.ORIENTATION_LANDSCAPE) {
                GridLayoutManager(view.context, resources.getInteger(R.integer.LANDSCAPE_COLS))
            } else {
                GridLayoutManager(view.context, resources.getInteger(R.integer.PORTRAIT_COLS))
            }
        binding.recyclerRectangle.layoutManager = layoutManager
//        var count = resources.getInteger(R.integer.PER_PAGE_ITEMS)
//
//        savedInstanceState?.let { bundle ->
//            count = bundle.getInt("COUNT_RECT")
//        }
        var rvAdapter: RvAdapter = RvAdapter(viewModel.PictureList.value!!)
        binding.recyclerRectangle.adapter = rvAdapter
        binding.addButton.setOnClickListener {
            viewModel.addPicture()
        }

        viewModel.PictureList.observe(viewLifecycleOwner) {
            rvAdapter.upDateList(it)
        }
    }

}